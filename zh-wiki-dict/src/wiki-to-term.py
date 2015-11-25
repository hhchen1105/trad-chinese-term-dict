#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Desc

'''

# Hung-Hsuan Chen <hhchen1105@gmail.com>
# Creation Date : 10-23-2015
# Last Modified:

import json
import logging
import sys

import gflags
import opencc
import sqlalchemy

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


def is_all_chinese_chars(s):
    return all(u'\u4e00' <= c <= u'\u9fff' for c in s)


def wiki_to_term():
    mariadb_info = json.load(open('../etc/mariadb_settings.json'))
    engine = sqlalchemy.create_engine('mysql+mysqldb://%s:%s@%s/%s' % (
            mariadb_info['user'], mariadb_info['pwd'], mariadb_info['host'], mariadb_info['db']))
    connection = engine.connect()

    print 'Processing wikipedia titles'
    # details of namespace: https://en.wikipedia.org/wiki/Wikipedia:Namespace
    valid_wiki_namespace = [0, 118]
    result = connection.execute("""SELECT page_title FROM page WHERE page_namespace in (%s)""" % (','.join([str(s) for s in valid_wiki_namespace])))
    terms = set()
    for i, row in enumerate(result, 1):
        sys.stdout.write('\r%i / %i' % (i, result.rowcount))
        title_unicode = row['page_title'].decode('utf-8')
        if is_all_chinese_chars(title_unicode) and len(title_unicode) > 1:
            terms.add(opencc.convert(title_unicode.encode('utf-8'), 'zhs2zhtw_p.ini'))
    connection.close()

    sys.stdout.write('\nSorting and saving results...')
    with open('../var/tw-wiki-dict.dict', 'w') as f_out:
        for t in sorted(terms):
            f_out.write('%s\n' % (t.encode('utf-8')))
    print 'Done'


def main(argv):
    check_args(argv)

    wiki_to_term()


if __name__ == "__main__":
    main(sys.argv)


