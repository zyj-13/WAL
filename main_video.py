from download_single import download_single
import argparse
import time

parser = argparse.ArgumentParser(description='Start downloading')
parser.add_argument('data', help='path to url file')


def main():
    args = parser.parse_args()


    # ----------------------- read vids
    fname = args.data
    with open(fname) as f:
        vids = f.readlines()

    vids = [x.strip() for x in vids] 

    


    # ------------------------ download
    for i in range(len(vids)):
        print('downloading video No.%d' % i)
        try:
            download_single(vids[i])
        except:
            print("video No.%d download failed and pass." % i)
        time.sleep(10)

if __name__ == '__main__': 
    main()


