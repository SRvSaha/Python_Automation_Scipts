#
#   @author      : SRvSaha
#   Filename     : fire_microblog_extract.py
#   Timestamp    : 16:58 25-August-2016 (Thursday)
#   Description  : To extract some semi-xml type of data
#

import re
import sys

filename = sys.argv[1]
with open(filename) as f:
    lines = f.read()
list_num = []
list_title = []
list_narr = []
list_desc = []
list_top = []
num = re.compile('<num>')
title = re.compile('<title>')
narr = re.compile('<narr>')
desc = re.compile('<desc>')
top = re.compile('</top>')
for item in num.finditer(lines):
    list_num.append(item.start())
for item in title.finditer(lines):
    list_title.append(item.start())
for item in desc.finditer(lines):
    list_desc.append(item.start())
for item in narr.finditer(lines):
    list_narr.append(item.start())
for item in top.finditer(lines):
    list_top.append(item.start())

f = open("fire_microblog_extraced.txt",'w');
for i in range(len(list_num)):
    num = ("".join(((lines[list_num[i]:list_title[i]]).split(':'))[1:])).strip()
    title = (" ".join(((lines[list_title[i]:list_desc[i]]).split(' '))[1:])).strip()
    desc = ("".join(((lines[list_desc[i]:list_narr[i]]).split(':'))[1:])).strip()
    narr = ("".join(((lines[list_narr[i]:list_top[i]]).split(':'))[1:])).strip()
    f.write(num+'\t'+title+'\t'+desc+'\t'+narr+'\n'+'\n')
f.close()
print("Operation Successful :)")
