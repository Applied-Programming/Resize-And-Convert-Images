import os, sys, glob
from PIL import Image

size = (299, 299)
filetypes =['*.jpg','*.jpeg']

def resize(infile):
    outfile = os.path.splitext(infile)[0] + ".png"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            old_im_size = im.size
            
            ## By default, black colour would be used as the background for padding!
            new_im = Image.new("RGB", size)

            new_im.paste(im, ((size[0]-old_im_size[0])/2,
                              (size[1]-old_im_size[1])/2))
            
            new_im.save('Resized_Images/' + outfile, "PNG")
        except IOError:
            print "Cannot resize '%s'" % infile

for filetype in filetypes:
    for single_jpg in glob.glob(filetype):
        print single_jpg
        resize(single_jpg)

print "Done"
