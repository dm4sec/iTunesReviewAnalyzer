# 1. Get started
## 1.1 Prerequisites
```
$ sudo apt-get install libcurl4-openssl-dev
$ sudo apt-get install libssl-dev
$ git clone --recurse-submodules https://github.com/dm4sec/iTunesReviewAnalyzer.git
$ cd iTunesReviewAnalyzer
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

# 2. Modules
## 2.1 EPFData
Download, parse and feed [EPF](https://feeds.itunes.apple.com/) data.
```
usage: EPFDataProc.py [-h] --username USERNAME --password PASSWORD

optional arguments:
  -h, --help           show this help message and exit
  --username USERNAME  Username for accessing EPF data.
  --password PASSWORD  Password for accessing EPF data.

e.g., python3 EPFDataProc.py --username=username --password=123456
```

## 2.2. ReviewCrawler
Get user's reviews and related stuff.

## 2.3. Analyzer
Use a variety of modules, including LDA, FP_Growth, BTM, etc. to analysis the review. 

# 3. TODO
3.1. Specified region can access limited resource. We need region information to detour the request.
```
https://apps.apple.com/us/genre/ios/id36
https://apps.apple.com/cn/genre/ios/id36
```
3.2. record lifetime of the app.