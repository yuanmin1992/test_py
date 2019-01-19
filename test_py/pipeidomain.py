#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re

def getUrlFromFile(fobj):
    regex = re.compile(r"(\w+(-\w+)*)(\.(\w+(-\w+)*))*(\?\s*)?$")
    urls = regex.search(fobj).group()
    print(urls)
    return urls

fobj = "http://www.s-tore.logitech.com.cn"
getUrlFromFile(fobj)