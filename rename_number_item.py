#Python 3

import sys
import os
from datetime import datetime
from shutil import copyfile
import os.path
import threading
import time

LOG = 0

file_data = ""
argv_len = len(sys.argv)
if (argv_len == 2):
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        for line in f:
            #line=line.strip('\n')
            found_end = line.find("\": {")
            found_start = line.find("\"")
            if (found_end != -1):
                #print (line[found_start+1:found_end])
                i = int(line[found_start+1:found_end])
                #42 之後的 id 全部+1
                if (i >= 42):
                    line = line.replace(str(i), str(i+1))
                    print (line)
            file_data += line
    f.close()
    with open(sys.argv[1], "w", encoding="utf-8") as f:
        f.write(file_data)
else:
    print ("argument length: " + (str)(argv_len) + " is wrong")
    print ("Command example: python " + sys.argv[0] + " main.log")