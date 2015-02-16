__author__ = 'josh'
from pelican import signals
import os, shutil
import logging

logger = logging.getLogger(__name__)

def direct_copy(pel):
    '''
    Copies any/all static files in a given directory in the content path unmodified into the main output path.

    An example of usage is to inject a .htaccess file into the output directory. By default, files will be copied over
    from `content/direct_copy`, though this is configurable by defining `DIRECT_COPY_SOURCE` in your settings.

    If needed, directories will be created. If a file which is to be copied already exists, will skip that particular
    file and print a note
    :param pel:
    :return:
    '''
    direct_copy_dirname = pel.settings.get('DIRECT_COPY_SOURCE') or 'direct_copy'
    static_dir = os.path.join(pel.settings.get('PATH'), direct_copy_dirname)
    output_dir = pel.settings.get('OUTPUT_PATH')
    for root, dirs, files in os.walk(static_dir):
        for f in files:
            src_file = os.path.join(root, f)
            dest_dir = root.replace(static_dir, output_dir)
            dest_file = os.path.join(dest_dir, f)
            if not os.path.isdir(dest_dir):
                os.mkdir(dest_dir)
            if os.path.isfile(dest_file):
                logger.warning("%s already exists; skipping" % dest_file)
                continue
            shutil.copy2(src_file, dest_file)

def register():
    signals.finalized.connect(direct_copy)