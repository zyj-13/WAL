import subprocess
import os
import argparse

parser = argparse.ArgumentParser(description='download subtitles')
parser.add_argument('data', help='path to url file')


def main():
    args = parser.parse_args()

    # ------------------ get urls
    fname = args.data
    with open(fname) as f:
        vids = f.readlines()

    vids = [x.strip() for x in vids]


    # -------------------- download subtitles

    for i in range(len(vids)):
        cmd = 'youtube-dl --write-auto-sub --sub-format "vtt" -o "data/subtitle/' + vids[i] + '" --skip-download https://www.youtube.com/watch?v=' + vids[i]
        os.system(cmd)


if __name__ == '__main__': 
    main()


