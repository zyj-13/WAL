import os
import codecs

# get vids
with open('data/url/url.txt') as f:
    vids = f.readlines()
vids = [x.strip() for x in vids]

for v in range(len(vids)):

  # get subtitles
  fname = 'data/subtitle_processed/%s.txt' % vids[v]
  vname = 'data/video/%s.mp4' % vids[v]
  with open(fname) as f:
    subt = f.readlines()
 
  subt = [x.strip() for x in subt]


  # open a txt file
  cmd_dir = 'mkdir data/dataset/%s' % vids[v]
  os.system(cmd_dir)
  subname = 'data/dataset/%s/%s.txt' % (vids[v], vids[v])
  text_sub = open(subname, "w")



  # cut
  idx_sent = 0
  for sid in range(len(subt)):
    #print('sid %s' % subt[sid])
    if sid % 4 == 0:
      start = subt[sid]
      #print(start)    
    elif sid % 4 == 1:
      end = subt[sid]
      #print(end)
    elif sid % 4 == 2:
      sent = subt[sid]
    elif sid % 4 == 3 and sent and sent[0] is not '[':  
      print(sent)
     
      text_sub.write("%d %s\n" % (idx_sent,sent)) 
 
      cmd = 'ffmpeg -i data/video/%s.mp4 -ss %s -to %s -async 1 data/dataset/%s/%d.mp4' % (vids[v], start, end, vids[v], idx_sent)
      #print(cmd)
      os.system(cmd)
      idx_sent += 1
 
  text_sub.close()




