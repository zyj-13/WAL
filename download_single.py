from pytube import YouTube
import os

def download_single(vid):
    
    vtype = 'mp4'    
    vRes = '360p'

    yt = YouTube('https://www.youtube.com/watch?v=%s' % vid)
    
    # download
    yt.streams.filter(subtype=vtype,res=vRes).first().download()
    #print(yt.streams.filter(res='240p').all())

    # rename
    fileName = yt.streams.first().default_filename
    fileName = fileName.split('.', 1)[0]+'.mp4'
    os.rename(fileName, 'data/video/%s.%s' % (vid, vtype) )
    













