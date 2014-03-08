__author__ = 'wu'

import re
import urllib
aa = re.compile(r'a(.*?)b')

print urllib.urlopen("http://192.168.1.109:8000/home/rege/login/").read()
