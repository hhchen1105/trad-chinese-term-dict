#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Desc

'''

# Hung-Hsuan Chen <hhchen1105@gmail.com>
# Creation Date : 09-30-2015
# Last Modified:

import logging
import json
import re
import sys

import gflags

FLAGS = gflags.FLAGS
gflags.DEFINE_string('arg1', '', '')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def usage(cmd):
    logger.warn('Usage: %s --arg1="VAL"' % (cmd))
    return


def check_args(argv):
    try:
        argv = FLAGS(argv)
    except gflags.FlagsError:
        logger.error(FLAGS, exc_info=True)

    #if FLAGS.arg1 == '':
    #    usage(argv[0])
    #    logger.error('flag --arg1 cannot be empty', exc_info=True)
    #    raise


def process_special_chars(title):
    unicode_str = re.findall('\{\[[0-9|a-f]+\]\}', title)
    if unicode_str != [ ]:
        # TODO: occasionally rare words are rendered incorrectly.
        # I ignore these terms, but I should fix this when I have time
        # title = process_rare_words(title)
        title = ''
    return title


def main(argv):
    check_args(argv)

    with open('../var/tw-edu-dict.dict', 'w') as f:
        # parse from Taiwan Ministry of Education dictionary
        d = json.load(open('../var/dict-revised.json'))
        for i, ele in enumerate(d):
            title = ele['title']
            title = process_special_chars(title)
            if len(title) > 1:
                f.write("%s\n" % (title.encode("utf-8")))

        # parse from other terms (e.g., 成語，諺語，地名，城市名，節日，節氣, etc.)
        for i, ele in enumerate(json.load(open('../var/dict-cat.json'))):
            for title in ele['entries']:
                title = process_special_chars(title)
                if len(title) > 1:
                    f.write("%s\n" % (title.encode("utf-8")))


if __name__ == "__main__":
    main(sys.argv)


