#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys, os, os.path, glob, codecs
import re, json


def rename_list(pattern):
    #if pattern is None:
    p = re.compile(pattern)
    flist = glob.glob('*')
    flist.sort()
    for f in flist:
        mo = p.match(f)
        if mo:
            g = mo.groups()
            nf = 'c2' + g[0] + '.html'
            print 'mv %s %s' % (f, nf)

if __name__ == '__main__':
    args = sys.argv[1:]
    #rename_list(args[0] if args else None)
    with open(args[0]) as fp:
        j = json.load(fp)
        for k,v in j.items():
            print k, v

