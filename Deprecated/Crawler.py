#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Deprecated

import sys
import requests
import logging

logging.basicConfig(stream=sys.stdout, format="%(levelname)s: %(asctime)s: %(message)s", level=logging.INFO,
                    datefmt='%a %d %b %Y %H:%M:%S')
log = logging.getLogger(__name__)

# https://apps.apple.com/us/genre/ios/id36
# https://apps.apple.com/cn/genre/ios/id36

category = {
    "cn":
        [
            "务",
            "",
            ""
        ],
    "en":
        [
            "ios-games-music",
            "",
            ""
        ]
}


def getIDList(category, county):
    retMe = set()

    url = "https://itunes.apple.com/search?term={}&country={}&media=software&limit=10000".format(category, county)
    try:
        r = requests.get(url=url, verify=False, stream=True, timeout=10.0)
    except Exception as e:
        log.error("Requests.get error: {}".format(e))

    log.info(r.text)

    return retMe

def retriveReview(ID):
    retMe = set()

    url = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id={}&displayable-kind=11&startIndex=0&endIndex=100&sort=1&appVersion=current".format(ID)
    # url = "https://itunes.apple.com/WebObjects/MZStore.woa/wa/userReviewsRow?id=989673964&displayable-kind=11&startIndex=0&endIndex=100&sort=1&appVersion=current"
    request_headers = {
        # "Host": "itunes.apple.com",
        # "User-Agent": "iTunes/12.5.5 (Windows; Microsoft Windows 10.0 x64 (Build 18363); x64) AppleWebKit/7602.2015.0.18",
        # "Referer": "https://apps.apple.com/cn/app/%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80/id989673964?l=en",
        # "Cookie": "amia-16975256008=5LHzBEusuWx6kkPxXHYvzSvrZUGGgtFM2A7m/cW03P7N6ZwCUPM9WsRF1n0muOox7sz7Y37XZuyQlPrWKkVy1Q==; amp=+oWQJcjxLgRSYS8u9bpIwMWYPpceJPsNGRY9gecmGYR2mjXOjGRPIojPcEhheCMbIpDcmEjuwUEIqMc6Bt61nDMOBS2hOc+ga1UUf+oOSfM=; mt-asn-16975256008=2; mt-tkn-16975256008=AiqKNYupiJboU3LfQlq6dhQlbaF9SMB6sEcM8mO8Khc9aFymVxW+lnv9ssqF+twK65cMXo4n1BHtFUiEfrUnhTv7oDP8vnakcw/KRPA5IrgbGs0q282bTXY8oZKXrEFp/qlVllhmnzZusKsgTBDErsje6TRMLsMhjoUKT+IMWeeICeRt8NN8jfxL2oBgtSa+PTXDMJ8=; mt-tkn-16248681244=AlVXNFneLLzcly/8ofW/DX8UpQH02i5Nm09rKdGeR2bROM74xvF3RHB/XQH0XQyMG0rZkdH1KhzQXL+OXW0b0Zg/ZULSDJNktSJBFfX4tVToFRGf8ij0AqfH/0ZX8EVXsyK2lEivOkfpNMr6gXBpXyu6gPAnSvRaVRV2R7oZZoycN5ugw98pJrXLkobW5oD+m62NZgs=; mzf_in=3700056; itspod=70; vrep=CMizt54_EgQIBhAAEgQIDRAAEgQIAhAAEgQIBxAAEgQIBBAAEgQIARAAEgQIAxAAEgQICRAAEgQICBAAEgQIChAAEgQICxAAEgQIDBAAEgQIBRAA; mz_at0-16975256008=AwQAAAECAAHWuQAAAABgSeVowGf4rDpvXy319jTTUHsL4CO7FRA=; mz_at_ssl-16975256008=AwUAAAECAAHWuQAAAABgSeVoMqJObT9ZPDWGiy0dM+chSgclcIw=; pldfltcid=53693a5e34f54acaa78a62b3456645b1070; X-Dsid=16975256008; mz_at0-16248681244=AwQAAAECAAHWtgAAAABgPvyU9aUF0cPJzRAVb38EcegK/qREfkY=; mz_at_ssl-16248681244=AwUAAAECAAHWtgAAAABgPvyUlM3yKq4u1XDaiszn3BQMw3+Z9oI=",
        # "Accept-Language": "en-us",
        # "Origin": "https://apps.apple.com",
        # "X-Apple-I-MD-RINFO": "50660608",
        "X-Apple-Store-Front": "143465-2,32",
        # "X-Dsid": "16975256008",

    }

    try:
        r = requests.get(url=url, verify=False, stream=True, timeout=10.0, headers=request_headers)
    except Exception as e:
        log.error("Requests.get error: {}".format(e))

    log.info(r.text)

    return retMe


def main():
    # retriveReview("1449678434")

    getIDList("图书", "cn")


if __name__ == '__main__':
    main()