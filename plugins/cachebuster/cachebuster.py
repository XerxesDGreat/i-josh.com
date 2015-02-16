__author__ = 'josh'
import time
from pelican import signals

def bust_some_caches(generator):
    generator.context['CACHEBUST'] = str(int(time.time()))

def register():
    signals.article_generator_finalized.connect(bust_some_caches)