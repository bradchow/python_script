# remember to save CU log file to UTF-8 first, otherwise it will be failed.
# preview_callback_imu: DROP rate: 2.09 % (209 / 10000)
# CRA DROP rate: 0.17 % (7 / 4000))

import sys
import os
import datetime
from shutil import copyfile
import os.path

LOG = 0

ALL_KEYWORD = "[all]"
ZERO_KEYWORD = "[0]"
ONE_KEYWORD = "[1]"
TWO_KEYWORD = "[2]"
THREE_KEYWORD = "[3]"
FOUR_KEYWORD = "[4]"
FIVE_KEYWORD = "[5]"
SIX_KEYWORD = "[6]"
SEVEN_KEYWORD = "[7]"
GPU_KEYWORD = "[GPU]"
ACTIVE_KEYWORD = "Active"

TOTAL_TIMES = 0
ALL_times = 0
ZERO_times = 0
ONE_times = 0
TWO_times = 0
THREE_times = 0
FOUR_times = 0
FIVE_times = 0
SIX_times = 0
SEVEN_times = 0
GPU_times = 0

f_log = open(sys.argv[1], "r");

for line in f_log.readlines():
    line=line.strip('\n')
    has_active = line.find(ACTIVE_KEYWORD)
    if (has_active != -1):
	TOTAL_TIMES += 1
	#Check ALL
	all_start = line.find(ALL_KEYWORD)
	if (all_start != -1):
	    all_end = line.find(ZERO_KEYWORD)
	    if (LOG == 1):
	      print line
	    if (LOG == 1):
	      print line[all_start+5:all_end-2]
	    ALL_times += (float)(line[all_start+5:all_end-2])
	#Check ZERO
	zero_start = line.find(ZERO_KEYWORD)
	if (zero_start != -1):
	    zero_end = line.find(ONE_KEYWORD)
	    if (LOG == 1):
	      print line
	    if (LOG == 1):
	      print line[zero_start+5:zero_end-2]
	    ZERO_times += (float)(line[zero_start+5:zero_end-2])
	#Check ONE
	one_start = line.find(ONE_KEYWORD)
	if (one_start != -1):
	    one_end = line.find(TWO_KEYWORD)
	    if (LOG == 1):
	      print line
	    if (LOG == 1):
	      print line[one_start+5:one_end-2]
	    ONE_times += (float)(line[one_start+5:one_end-2])
	#Check TWO
	two_start = line.find(TWO_KEYWORD)
	if (two_start != -1):
	    two_end = line.find(THREE_KEYWORD)
	    if (LOG == 1):
	      print line
	    if (LOG == 1):
	      print line[two_start+5:two_end-2]
	    TWO_times += (float)(line[two_start+5:two_end-2])
	#Check THREE
	three_start = line.find(THREE_KEYWORD)
	if (three_start != -1):
	    three_end = line.find(FOUR_KEYWORD)
	    if (LOG == 1):
	      print line
	    if (LOG == 1):
	      print line[three_start+5:three_end-2]
	    THREE_times += (float)(line[three_start+5:three_end-2])
	#Check FOUR
	four_start = line.find(FOUR_KEYWORD)
	if (four_start != -1):
	    four_end = line.find(FIVE_KEYWORD)
	    if (LOG == 1):
	      print line
	    if (LOG == 1):
	      print line[four_start+5:four_end-2]
	    FOUR_times += (float)(line[four_start+5:four_end-2])
	#Check FIVE
	five_start = line.find(FIVE_KEYWORD)
	if (five_start != -1):
	    five_end = line.find(SIX_KEYWORD)
	    if (LOG == 1):
	      print line
	    if (LOG == 1):
	      print line[five_start+5:five_end-2]
	    FIVE_times += (float)(line[five_start+5:five_end-2])
	#Check SIX
	six_start = line.find(SIX_KEYWORD)
	if (six_start != -1):
	    six_end = line.find(SEVEN_KEYWORD)
	    if (LOG == 1):
	      print line
	    if (LOG == 1):
	      print line[six_start+5:six_end-2]
	    SIX_times += (float)(line[six_start+5:six_end-2])
	#Check SEVEN
	seven_start = line.find(SEVEN_KEYWORD)
	if (seven_start != -1):
	    seven_end = line.find(GPU_KEYWORD)
	    if (LOG == 1):
	      print line
	    if (LOG == 1):
	      print line[seven_start+5:seven_end-2]
	    SEVEN_times += (float)(line[seven_start+5:seven_end-2])
    
f_log.close()
print "[CPU run] total counts: %.3f" % (float)(TOTAL_TIMES)
print "[all] times: %.3f" % (float)(ALL_times) + ", [r_all] avg: %.3f" % ((float)(ALL_times) / (float)(TOTAL_TIMES)) + "%"
print "[0] times: %.3f" % (float)(ZERO_times) + ", [r_0] avg: %.3f" % ((float)(ZERO_times) / (float)(TOTAL_TIMES)) + "%"
print "[1] times: %.3f" % (float)(ONE_times) + ", [r_1] avg: %.3f" % ((float)(ONE_times) / (float)(TOTAL_TIMES)) + "%"
print "[2] times: %.3f" % (float)(TWO_times) + ", [r_2] avg: %.3f" % ((float)(TWO_times) / (float)(TOTAL_TIMES)) + "%"
print "[3] times: %.3f" % (float)(THREE_times) + ", [r_3] avg: %.3f" % ((float)(THREE_times) / (float)(TOTAL_TIMES)) + "%"
print "[4] times: %.3f" % (float)(FOUR_times) + ", [r_4] avg: %.3f" % ((float)(FOUR_times) / (float)(TOTAL_TIMES)) + "%"
print "[5] times: %.3f" % (float)(FIVE_times) + ", [r_5] avg: %.3f" % ((float)(FIVE_times) / (float)(TOTAL_TIMES)) + "%"
print "[6] times: %.3f" % (float)(SIX_times) + ", [r_6] avg: %.3f" % ((float)(SIX_times) / (float)(TOTAL_TIMES)) + "%"
print "[7] times: %.3f" % (float)(SEVEN_times) + ", [r_7] avg: %.3f" % ((float)(SEVEN_times) / (float)(TOTAL_TIMES)) + "%"
