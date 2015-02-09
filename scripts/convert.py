import os

c_dir=os.path.join('/home', 'josh', 'dev', 'i-josh.com', 'content')
src = os.path.join(c_dir, 'un')

for root, dirs, files in os.walk(src):
    for f in files:
        with open(os.path.join(root, f)) as pf:
            lines = pf.readlines()

        category = lines[4][2:].rstrip()
        new_body = [
            'Title: %s' % lines[0][2:],
            'Date: %s 09:00\n' % lines[3][2:].rstrip(),
            'Category: %s\n' % category,
            'Author: %s' % lines[1][2:]
        ]
        new_body.extend(lines[6:])

        with open(os.path.join(c_dir, category, f), 'w') as fh:
            fh.write(''.join(new_body))

