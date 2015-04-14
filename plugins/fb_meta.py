__author__ = 'josh'
from pelican import signals
import re
from types import *
try:
    from html.parser import HTMLParser
except:
    from HTMLParser import HTMLParser

def _get_from_meta(article, meta_key, attr):
    return article.metadata[meta_key] if meta_key in article.metadata else getattr(article, attr)

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def _get_description(article):
    if 'fbdescription' in article.metadata:
        fbdesc = article.metadata['fbdescription']
        desc = ' '.join(fbdesc) if type(fbdesc) is ListType else fbdesc
    else:
        desc = article.summary
    return strip_tags(desc)


img_pattern = re.compile(r'<img\s(.*\s)?src=[\'"](.*)[\'"].*>')
def _get_image_url(article):
    '''
    Fetches all the images in the provided content, which is an HTML string in Unicode
    '''
    if 'fbimage' in article.metadata:
        fb_image = '/'.join((article.settings.get('SITEURL'), article.metadata['fbimage']))
    else:
        images = img_pattern.findall(article.content)
        if len(images) < 1:
            fb_image = article.settings.get('HEADER_IMG_URL')
        elif 'fbimageindex' in article.metadata:
            try:
                fb_image = images[article.metadata['fbimageindex']][1]
            except:
                fb_image = images[0][1]
        else:
            fb_image = images[0][1]
    return fb_image


def generate_fb_meta_write_article(generator, *args, **kwargs):
    if 'FACEBOOK_OPENGRAPH_TAGS' in generator.settings and generator.settings.get('FACEBOOK_OPENGRAPH_TAGS'):
        article = kwargs['content']
        kwargs['content'].fb_opengraph_tags = {
            'image': _get_image_url(article),
            'title': _get_from_meta(article, 'fbtitle', 'title'),
            'description': _get_description(article)
        }

def register():
    signals.article_generator_write_article.connect(generate_fb_meta_write_article)