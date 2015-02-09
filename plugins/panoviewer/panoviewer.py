import json
import os
from pelican import signals

def add_panoviewer_post(generator):
    content_path = generator.settings.get('PATH')
    pano_content_path = os.path.join(content_path,'panorama')

    for article in generator.articles:
        if 'panogroup' not in article.metadata.keys():
            continue
        
        pano_group = article.metadata.get('panogroup')
        pano_data_file = os.path.join(pano_content_path, pano_group, 'details.json')
        if not os.path.isfile(pano_data_file):
            print 'no pano data file for %s' % pano_group
            continue
        
        with open(pano_data_file) as f:
            try:
                pano_details = json.loads(f.read())
            except e:
                print "exception found: %s" % e
                pano_details = None
        
        article.pano_details = pano_details
        article.pano_group = pano_group

def register():
    signals.article_generator_finalized.connect(add_panoviewer_post)
