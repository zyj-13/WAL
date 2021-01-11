

fname = 'data/subtitle/list_subtitle.txt';
with open(fname) as f:
    vids = f.readlines()
vids = [x.strip() for x in vids]


fname = 'data/url/url.txt'
text_file = open(fname, "w")

for i in range(len(vids)):
  vid = vids[i].split('/')[1].split('.')[0]
  text_file.write("%s\n" % vid)

text_file.close()

