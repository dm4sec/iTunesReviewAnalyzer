import sys
import logging
import json
from header import db
import requests
import traceback
from threading import Thread

logging.basicConfig(stream=sys.stdout, format="%(levelname)s: %(asctime)s: %(message)s", level=logging.INFO,
                    datefmt='%a %d %b %Y %H:%M:%S')
log = logging.getLogger(__name__)


app_category = {
    "cn":
        [
            "艺术与摄影"
        ],
    "us":
        [
            "ios-games-music"
        ]
}


def get_header():
    header = {"Host": "itunes.apple.com",
              "User-Agent": "iTunes/12.0.1 (Windows; Microsoft Windows 8 x64 Business Edition (Build 9200)) AppleWebKit/7600.1017.0.24",
              "Accept": "*/*",
              "X-Apple-Store-Front": "143465-19,28",
              "Referer": "https://apps.apple.com/cn/app/%E6%B4%AA%E6%81%A9%E5%8F%8C%E8%AF%AD%E7%BB%98%E6%9C%AC/id1235986511",
              "Origin": "https://apps.apple.com",
              "Cookie": "xp_ab=1#WqjkRLH+-2+TCEF_ea01#d5VBr6w+-2+yAr0o5S03#yNFpB6B+-2+c9imSgD01; xp_abc=TCEF_ea01; xp_ci=3zvQJLNz4afz5MFzCawzqBEFV5uS",
              "Accept-Language": "zh-cn, zh;q=0.75, en-us;q=0.50, en;q=0.25",
              "X-Apple-Tz": "28800",
              "Accept-Encoding": "gzip, deflate",
              "Connection": "keep-alive",
              "Proxy-Connection": "keep-alive"}
    return header


class CommentCrawler(Thread):
    host = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id={}&displayable-kind=11&startIndex={}&endIndex={}&sort=-1&appVersion=all"

    def __init__(self, task_id):
        Thread.__init__(self)
        if not task_id:
            raise Exception
        self.__id = task_id

    def __request_with_id(self):
        start = 0
        step = 500

        stop = False
        cnt = 0

        while 1:
            r = requests.request("GET", self.host.format(self.__id, start, start + step), headers=get_header())
            try:
                if r.text:
                    ret = json.loads(r.text)["userReviewList"]
                else:
                    return
            except:
                log.error("Error in id={}".format(self.__id))
                log.error("Error response:\n{}".format(r.text))
                traceback.print_exc()
                return

            start += step
            if len(ret) == 0:
                break

            for one in ret:
                if db.get_collection("comment").find_one({"userReviewId": one["userReviewId"]}):
                    stop = True
                    break
                cnt += 1
                one["application_id"] = self.__id
                db.get_collection("comment").insert_one(one)

            if stop:
                break

        log.info("Done with id={}, got {} new comment(s).".format(self.__id, cnt))

    def run(self):
        self.__request_with_id()


class IdCrawler(object):
    host = "https://itunes.apple.com/search?term={}&country={}&media=software&limit=10000"

    def __init__(self):
        pass

    def __request_with_id(self, category, term):
        r = requests.get(self.host.format(category, term))
        print(r.text)
        data = json.loads(r.text)["results"]
        cnt = 0
        for one in data:
            if not db.get_collection("app").find_one({"trackId": one["trackId"]}):
                db.get_collection("app").insert_one({"trackId": one["trackId"], "bundleId": one["bundleId"]})
                cnt += 1
        log.info("Got {} new apps.".format(cnt))

    def run(self):
        for term in app_category.keys():
            for category in app_category[term]:
                log.info("Processing: {}-{}".format(term, category))
                self.__request_with_id(category, term)


if __name__ == "__main__":
    thread = CommentCrawler("1505065896")
    thread.start()

    # c = IdCrawler()
    # c.run()
