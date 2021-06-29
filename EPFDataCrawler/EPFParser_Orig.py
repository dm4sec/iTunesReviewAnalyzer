import time

from header import db
import datetime


sep_field = chr(1)
sep_record = chr(2)
block = 1024

key_list = ["export_date",
            "application_id",
            "title",
            "recommended_age",
            "artist_name",
            "seller_name",
            "company_url",
            "support_url",
            "view_url",
            "artwork_url_large",
            "artwork_url_small",
            "itunes_release_date",
            "copyright",
            "description",
            "version",
            "itunes_version",
            "download_size"]


def parse_data(s):
    one = {}
    tup = s.split(sep_field)
    for i in range(len(tup)):
        one[key_list[i]] = tup[i]
    one["export_date"] = datetime.datetime.fromtimestamp(int(one["export_date"])/1000.0)
    print("[-] Inserting: {}".format(one["title"]))
    db.get_collection("app").insert_one(one)


def build(file):
    content = ""

    with open(file, "r") as f:
        while 1:
            seg = f.read(block)
            if not seg:
                break
            content += seg
            sep = content.find(sep_record)
            if sep >= 0:
                data = content[0: sep]
                if not data.startswith("#") and not data[1] == "#":
                    parse_data(data[1:])
                content = content[sep+len(sep_record):]


if __name__ == "__main__":
    build("/home/demo/Downloads/application")
