import os
from PIL import Image

content_dir = os.path.realpath(os.path.join(os.getcwd(), '..', 'content'))
src = os.path.join(content_dir, 'images_source')
dest = os.path.join(content_dir, 'images')
size = (1000,1000)

print 'copying files from %s to %s' % (src, dest)

for root, dirs, files in os.walk(src):
    for f in files:
        base, ext = os.path.splitext(os.path.basename(f))
        target_f = '.'.join([base.lower(), 'jpg'])
        if os.path.isfile(os.path.join(dest, target_f)):
            print 'file %s exists; chickening out' % f
            continue
        im = Image.open(os.path.join(root, f))
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(os.path.join(dest, target_f))
        print 'thumbnail created for %s; image %s saved' % (f, target_f)
