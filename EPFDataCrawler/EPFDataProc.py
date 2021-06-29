import argparse
import sys
import os

sys.path.append(os.pardir)
sys.path.append("../../")

# from EPFDownloader.epf_downloader import EPFDownloader
from EPFDownloader.epf_downloader_full import EPFDowloaderFull
from EPFDownloader.epf_downloader_incremental import EPFDowloaderIncremental

def main():


    parser = argparse.ArgumentParser()
    parser.add_argument('--username', required=True, help="Username for accessing EPF data.")
    parser.add_argument('--password', required=True, help="Password for accessing EPF data.")

    args = parser.parse_args()

    EPFDataPath = "./EPFData"
    if not os.path.exists(EPFDataPath):
        os.mkdir(EPFDataPath)

    epfDataDownloaderFull = EPFDowloaderFull(args.username, args.password, EPFDataPath)

    r = epfDataDownloaderFull.perform_download()
    if r != "":
        print("foo")


if __name__ == "__main__":
    sys.exit(main())
