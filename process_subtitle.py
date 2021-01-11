
import webvtt



with open('data/url/url.txt') as f:
    vids = f.readlines()
vids = [x.strip() for x in vids]



for i in range(len(vids)):
  text_file = open('data/subtitle_processed/%s.txt' % vids[i] , "w")

  block = 1
  for caption in webvtt.read('data/subtitle/%s.en.vtt' % vids[i]): 
    if block == 1:
      #text_file.write('\n')
      text_file.write(caption.start)
    else:
      text_file.write('\n')
      text_file.write(caption.end) 

      text_file.write('\n')
      text_file.write(caption.text)
      text_file.write('\n')
      block = 0
    
    block += 1
 
  text_file.close()
  print('processing subtitle No. %d ...\n' % i)

  


  

