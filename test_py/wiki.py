# coding=utf-8
# 引用开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

resp = urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
soup = BeautifulSoup(resp,"html.parse")
print soup