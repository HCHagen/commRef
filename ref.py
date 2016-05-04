#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from sys import exit
from sys import argv

def srch(srchStr):
    refObj = json.loads(open(os.path.dirname(os.path.realpath(__file__))+'/commRef.json').read())
    ret = "\n"
    for key, value in refObj.iteritems():
        if srchStr.lower() in value.lower() or srchStr.lower() in key.lower():
            ret += '\033[1m' + str(key) + ":\t" + '\033[0m' + str(value) + ".\n"
    
    return ret

print (srch(argv[1]) if len(argv) > 1 else "\nMissing argument\n").format()
