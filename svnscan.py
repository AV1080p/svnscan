#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import requests
r = requests.get('http://www.baidu.com/.svn/entries')
#print r.headers
get=r.text.split('\n')
dir=[get[i-1] for i in range(len(get)) if get[i]=='dir' and get[i-1]!='']
file=[get[i-1] for i in range(len(get)) if get[i]=='file' and get[i-1]!='']
print dir
print file