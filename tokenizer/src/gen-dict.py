#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Desc

'''

# Hung-Hsuan Chen <hhchen1105@gmail.com>
# Creation Date : 10-28-2015
# Last Modified:

import logging
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


def main(argv):
    check_args(argv)

    all_terms = set()
    dic_srcs = ['../../moe-dict/var/tw-edu-dict.dict', '../../zh-wiki-dict/var/tw-wiki-dict.dict']
    for dic_src in dic_srcs:
        with open(dic_src) as f_src:
            for line in f_src:
                all_terms.add(line.strip().decode('utf-8'))

    with open('../var/tw-dict.dict', 'w') as f_write:
        for term in sorted(all_terms):
            f_write.write('%s\n' % (term.encode('utf-8')))


if __name__ == "__main__":
    main(sys.argv)


