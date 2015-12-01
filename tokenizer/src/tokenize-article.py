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
import jieba

FLAGS = gflags.FLAGS
gflags.DEFINE_string('content', '', '')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def usage(cmd):
    logger.warn('Usage: %s --content="content to tokenize"' % (cmd))
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


def is_chinese_char(w):
    return u'\u4e00' <= w <= u'\u9fff'


def keep_only_chinese_and_alphanumeric(contents):
    cleaned_contents = ''
    for w in contents:
        if is_chinese_char(w) or w.isalnum():
            cleaned_contents += w
        else:
            cleaned_contents += ' '
    return cleaned_contents


def show_terms(content, min_len=2):
    content = keep_only_chinese_and_alphanumeric(content)
    for term in jieba.cut(content, cut_all=False):    # accurate mode
        if len(term) >= min_len and term.strip() != '':
            print term


def main(argv):
    check_args(argv)

    print 'Loading dictionary...'
    jieba.load_userdict('../var/tw-dict.dict')

    print 'Tokenizing...'
    print 'Result:'
    show_terms(FLAGS.content.decode('utf-8'), min_len=2)


if __name__ == "__main__":
    main(sys.argv)


