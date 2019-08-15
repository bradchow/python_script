#!/usr/bin/python
# -*- coding: utf-8 -*-
#example: gen_md5.py system.img
# it will generate md5 string and have save to .md5 file 

import sys
import hashlib

# 輸入檔案名稱
filename = sys.argv[1]

m = hashlib.md5()

with open(filename, "rb") as f:
  # 分批讀取檔案內容，計算 MD5 雜湊值
  for chunk in iter(lambda: f.read(4096), b""):
    m.update(chunk)

h = m.hexdigest()
print(h)

f = open(filename+".md5","w+")
f.write(h)
f.close();