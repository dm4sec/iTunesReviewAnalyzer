from base.Crawler import CommentCrawler
from config import THREAD_NUM
from header import db
import threading
import time
import queue

q = queue.Queue(0)


def prepare():
    for one in db.get_collection("app").find({}, {"application_id": 1}):
        q.put(one["application_id"])


def start():
    threads = []

    while 1:
        # check alive
        for thread in threads:
            thread: CommentCrawler
            if not thread.is_alive():
                threads.pop(threads.index(thread))

        # create crawler threads
        for i in range(THREAD_NUM - len(threads)):
            try:
                crawler = CommentCrawler(q.get(block=False))
                crawler.start()
                threads.append(crawler)
                time.sleep(0.2)
            except:
                print("[!] All done.")
                time.sleep(5)
                exit()

        time.sleep(1)


if __name__ == "__main__":
    print("[*] Loading app id ...")
    prepare()
    print("[-] Done.")
    start()
