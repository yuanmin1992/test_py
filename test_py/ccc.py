#! /usr/bin/env python
# -*- coding: utf-8 -*-

import  urllib.request

response = urllib.request.urlopen("https://www.python.org")
print(response.read().decode('utf-8'))
# print(type(response))
print(response.status)
# print(response.text)
# print(response.getheaders())
print(response.getheader("Content-Length"))