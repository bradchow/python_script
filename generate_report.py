import sys
import os
from datetime import datetime
from shutil import copyfile
import os.path
import threading
import time

LOG = 0

CPU_IDLE_LOADING_AVG_ALL = "[i_all] avg:"
CPU_IDLE_LOADING_AVG_CORE_0 = "[i_0] avg:"
CPU_IDLE_LOADING_AVG_CORE_1 = "[i_1] avg:"
CPU_IDLE_LOADING_AVG_CORE_2 = "[i_2] avg:"
CPU_IDLE_LOADING_AVG_CORE_3 = "[i_3] avg:"
CPU_IDLE_LOADING_AVG_CORE_4 = "[i_4] avg:"
CPU_IDLE_LOADING_AVG_CORE_5 = "[i_5] avg:"
CPU_IDLE_LOADING_AVG_CORE_6 = "[i_6] avg:"
CPU_IDLE_LOADING_AVG_CORE_7 = "[i_7] avg:"
CPU_IDLE_AVG_ALL_LIST = []
CPU_IDLE_AVG_CORE_0_LIST = []
CPU_IDLE_AVG_CORE_1_LIST = []
CPU_IDLE_AVG_CORE_2_LIST = []
CPU_IDLE_AVG_CORE_3_LIST = []
CPU_IDLE_AVG_CORE_4_LIST = []
CPU_IDLE_AVG_CORE_5_LIST = []
CPU_IDLE_AVG_CORE_6_LIST = []
CPU_IDLE_AVG_CORE_7_LIST = []

CPU_RUN_LOADING_AVG_ALL = "[r_all] avg:"
CPU_RUN_LOADING_AVG_CORE_0 = "[r_0] avg:"
CPU_RUN_LOADING_AVG_CORE_1 = "[r_1] avg:"
CPU_RUN_LOADING_AVG_CORE_2 = "[r_2] avg:"
CPU_RUN_LOADING_AVG_CORE_3 = "[r_3] avg:"
CPU_RUN_LOADING_AVG_CORE_4 = "[r_4] avg:"
CPU_RUN_LOADING_AVG_CORE_5 = "[r_5] avg:"
CPU_RUN_LOADING_AVG_CORE_6 = "[r_6] avg:"
CPU_RUN_LOADING_AVG_CORE_7 = "[r_7] avg:"
CPU_RUN_AVG_ALL_LIST = []
CPU_RUN_AVG_CORE_0_LIST = []
CPU_RUN_AVG_CORE_1_LIST = []
CPU_RUN_AVG_CORE_2_LIST = []
CPU_RUN_AVG_CORE_3_LIST = []
CPU_RUN_AVG_CORE_4_LIST = []
CPU_RUN_AVG_CORE_5_LIST = []
CPU_RUN_AVG_CORE_6_LIST = []
CPU_RUN_AVG_CORE_7_LIST = []

IMU_DROP_TOTAL_KEYWORD = "IMU total miss:"
IMU_TOTAL_KEYWORD = "IMU total:"
IMU_DROP_RATE_KEYWORD = "IMU drop rate:"
IMU_DROP_TOTAL_LIST = []
IMU_TOTAL_LIST = []
IMU_DROP_RATE_LIST = []

CRA_DROP_TOTAL_KEYWORD = "CRA total miss:"
CRA_TOTAL_KEYWORD = "CRA total:"
CRA_DROP_RATE_KEYWORD = "CRA drop rate:"
CRA_DROP_TOTAL_LIST = []
CRA_TOTAL_LIST = []
CRA_DROP_RATE_LIST = []

CRB_DROP_TOTAL_KEYWORD = "CRB total miss:"
CRB_TOTAL_KEYWORD = "CRB total:"
CRB_DROP_RATE_KEYWORD = "CRB drop rate:"
CRB_DROP_TOTAL_LIST = []
CRB_TOTAL_LIST = []
CRB_DROP_RATE_LIST = []

MRCAM1_DROP_TOTAL_KEYWORD = "CAM1 total drop count:"
MRCAM1_TOTAL_KEYWORD = "CAM1 total counts:"
MRCAM1_DROP_RATE_KEYWORD = "drop rate:"
MRCAM1_DROP_TOTAL_LIST = []
MRCAM1_TOTAL_LIST = []
MRCAM1_DROP_RATE_LIST = []

MRCAM2_DROP_TOTAL_KEYWORD = "CAM2 total drop count:"
MRCAM2_TOTAL_KEYWORD = "CAM2 total counts:"
MRCAM2_DROP_RATE_KEYWORD = "drop rate:"
MRCAM2_DROP_TOTAL_LIST = []
MRCAM2_TOTAL_LIST = []
MRCAM2_DROP_RATE_LIST = []

argv_len = len(sys.argv)
if (argv_len == 2):
    f_log = open(sys.argv[1], "r");
        
    for line in f_log.readlines():
	line=line.strip('\n')
	#CPU idle all loading
	cpu_idle_loading_avg_all_found = line.find(CPU_IDLE_LOADING_AVG_ALL)
	if (cpu_idle_loading_avg_all_found != -1):
	    value = line[cpu_idle_loading_avg_all_found+13:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_IDLE_AVG_ALL_LIST.append(value)
	    continue
	#CPU idle core 0 loading
	cpu_idle_loading_avg_core_0_found = line.find(CPU_IDLE_LOADING_AVG_CORE_0)
	if (cpu_idle_loading_avg_core_0_found != -1):
	    value = line[cpu_idle_loading_avg_core_0_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_IDLE_AVG_CORE_0_LIST.append(value)
	    continue
	#CPU idle core 1 loading
	cpu_idle_loading_avg_core_1_found = line.find(CPU_IDLE_LOADING_AVG_CORE_1)
	if (cpu_idle_loading_avg_core_1_found != -1):
	    value = line[cpu_idle_loading_avg_core_1_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_IDLE_AVG_CORE_1_LIST.append(value)
	    continue
	#CPU idle core 2 loading
	cpu_idle_loading_avg_core_2_found = line.find(CPU_IDLE_LOADING_AVG_CORE_2)
	if (cpu_idle_loading_avg_core_2_found != -1):
	    value = line[cpu_idle_loading_avg_core_2_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_IDLE_AVG_CORE_2_LIST.append(value)
	    continue
	#CPU idle core 3 loading
	cpu_idle_loading_avg_core_3_found = line.find(CPU_IDLE_LOADING_AVG_CORE_3)
	if (cpu_idle_loading_avg_core_3_found != -1):
	    value = line[cpu_idle_loading_avg_core_3_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_IDLE_AVG_CORE_3_LIST.append(value)
	    continue
	#CPU idle core 4 loading
	cpu_idle_loading_avg_core_4_found = line.find(CPU_IDLE_LOADING_AVG_CORE_4)
	if (cpu_idle_loading_avg_core_4_found != -1):
	    value = line[cpu_idle_loading_avg_core_4_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_IDLE_AVG_CORE_4_LIST.append(value)
	    continue
	#CPU idle core 5 loading
	cpu_idle_loading_avg_core_5_found = line.find(CPU_IDLE_LOADING_AVG_CORE_5)
	if (cpu_idle_loading_avg_core_5_found != -1):
	    value = line[cpu_idle_loading_avg_core_5_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_IDLE_AVG_CORE_5_LIST.append(value)
	    continue
	#CPU idle core 6 loading
	cpu_idle_loading_avg_core_6_found = line.find(CPU_IDLE_LOADING_AVG_CORE_6)
	if (cpu_idle_loading_avg_core_6_found != -1):
	    value = line[cpu_idle_loading_avg_core_6_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_IDLE_AVG_CORE_6_LIST.append(value)
	    continue
	#CPU idle core 7 loading
	cpu_idle_loading_avg_core_7_found = line.find(CPU_IDLE_LOADING_AVG_CORE_7)
	if (cpu_idle_loading_avg_core_7_found != -1):
	    value = line[cpu_idle_loading_avg_core_7_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_IDLE_AVG_CORE_7_LIST.append(value)
	    continue
	#CPU running all loading
	cpu_running_loading_avg_all_found = line.find(CPU_RUN_LOADING_AVG_ALL)
	if (cpu_running_loading_avg_all_found != -1):
	    value = line[cpu_running_loading_avg_all_found+13:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_RUN_AVG_ALL_LIST.append(value)
	    continue
	#CPU running core 0 loading
	cpu_running_loading_avg_core_0_found = line.find(CPU_RUN_LOADING_AVG_CORE_0)
	if (cpu_running_loading_avg_core_0_found != -1):
	    value = line[cpu_running_loading_avg_core_0_found+11:len(line)-1]
	    if (LOG == 1):
		print line
		print value
	    CPU_RUN_AVG_CORE_0_LIST.append(value)
	    continue
	#CPU running core 1 loading
	cpu_running_loading_avg_core_1_found = line.find(CPU_RUN_LOADING_AVG_CORE_1)
	if (cpu_running_loading_avg_core_1_found != -1):
	    value = line[cpu_running_loading_avg_core_1_found+11:len(line)-1]	    
	    if (LOG == 1):
		print line
		print value
	    CPU_RUN_AVG_CORE_1_LIST.append(value)
	    continue
	#CPU running core 2 loading
	cpu_running_loading_avg_core_2_found = line.find(CPU_RUN_LOADING_AVG_CORE_2)
	if (cpu_running_loading_avg_core_2_found != -1):
	    value = line[cpu_running_loading_avg_core_2_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_RUN_AVG_CORE_2_LIST.append(value)
	    continue
	#CPU running core 3 loading
	cpu_running_loading_avg_core_3_found = line.find(CPU_RUN_LOADING_AVG_CORE_3)
	if (cpu_running_loading_avg_core_3_found != -1):
	    value = line[cpu_running_loading_avg_core_3_found+13:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_RUN_AVG_CORE_3_LIST.append(value)
	    continue
	#CPU running core 4 loading
	cpu_running_loading_avg_core_4_found = line.find(CPU_RUN_LOADING_AVG_CORE_4)
	if (cpu_running_loading_avg_core_4_found != -1):
	    value = line[cpu_running_loading_avg_core_4_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_RUN_AVG_CORE_4_LIST.append(value)
	    continue
	#CPU running core 5 loading
	cpu_running_loading_avg_core_5_found = line.find(CPU_RUN_LOADING_AVG_CORE_5)
	if (cpu_running_loading_avg_core_5_found != -1):
	    value = line[cpu_running_loading_avg_core_5_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_RUN_AVG_CORE_5_LIST.append(value)
	    continue
	#CPU running core 6 loading
	cpu_running_loading_avg_core_6_found = line.find(CPU_RUN_LOADING_AVG_CORE_6)
	if (cpu_running_loading_avg_core_6_found != -1):
	    value = line[cpu_running_loading_avg_core_6_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_RUN_AVG_CORE_6_LIST.append(value)
	    continue
	#CPU running core 7 loading
	cpu_running_loading_avg_core_7_found = line.find(CPU_RUN_LOADING_AVG_CORE_7)
	if (cpu_running_loading_avg_core_7_found != -1):
	    value = line[cpu_running_loading_avg_core_7_found+11:len(line)-1]
	    if (LOG == 1):
		print value
	    CPU_RUN_AVG_CORE_7_LIST.append(value)
	    continue
	#IMU drop count
	imu_drop_count = line.find(IMU_DROP_TOTAL_KEYWORD)
	if (imu_drop_count != -1):
	    imu_drop_count_end = line.find(",")
	    value = line[imu_drop_count+16:imu_drop_count_end]
	    IMU_DROP_TOTAL_LIST.append(value)
	#IMU total count
	imu_total_count = line.find(IMU_TOTAL_KEYWORD)
	if (imu_total_count != -1):
	    value = line[imu_total_count+11:]
	    IMU_TOTAL_LIST.append(value)
	#IMU drop rate
	imu_drop_rate = line.find(IMU_DROP_RATE_KEYWORD)
	if (imu_drop_rate != -1):
	    value = line[imu_drop_rate+15:]
	    IMU_DROP_RATE_LIST.append(value)
	#CRA drop count
	cra_drop_count = line.find(CRA_DROP_TOTAL_KEYWORD)
	if (cra_drop_count != -1):
	    cra_drop_count_end = line.find(",")
	    value = line[cra_drop_count+16:cra_drop_count_end]
	    CRA_DROP_TOTAL_LIST.append(value)
	#CRA total count
	cra_total_count = line.find(CRA_TOTAL_KEYWORD)
	if (cra_total_count != -1):
	    value = line[cra_total_count+11:]
	    CRA_TOTAL_LIST.append(value)
	#CRA drop rate
	cra_drop_rate = line.find(CRA_DROP_RATE_KEYWORD)
	if (cra_drop_rate != -1):
	    value = line[cra_drop_rate+15:]
	    CRA_DROP_RATE_LIST.append(value)
	#CRB drop count
	crb_drop_count = line.find(CRB_DROP_TOTAL_KEYWORD)
	if (crb_drop_count != -1):
	    crb_drop_count_end = line.find(",")
	    value = line[crb_drop_count+16:crb_drop_count_end]
	    CRB_DROP_TOTAL_LIST.append(value)
	#CRB total count
	crb_total_count = line.find(CRB_TOTAL_KEYWORD)
	if (crb_total_count != -1):
	    value = line[crb_total_count+11:]
	    CRB_TOTAL_LIST.append(value)
	#CRB drop rate
	crb_drop_rate = line.find(CRB_DROP_RATE_KEYWORD)
	if (crb_drop_rate != -1):
	    value = line[crb_drop_rate+15:]
	    CRB_DROP_RATE_LIST.append(value)
	#MRCAM1 drop count
	mrcam1_drop_count = line.find(MRCAM1_DROP_TOTAL_KEYWORD)
	if (mrcam1_drop_count != -1):
	    mrcam1_drop_count_end = line.find(",")
	    value = line[mrcam1_drop_count+23:mrcam1_drop_count_end]
	    MRCAM1_DROP_TOTAL_LIST.append(value)
	#MRCAM1 total count
	mrcam1_total_count = line.find(MRCAM1_TOTAL_KEYWORD)
	if (mrcam1_total_count != -1):
	    value = line[mrcam1_total_count+19:]
	    MRCAM1_TOTAL_LIST.append(value)
	#MRCAM1 drop rate
	mrcam1_drop_count = line.find(MRCAM1_DROP_TOTAL_KEYWORD)
	if (mrcam1_drop_count != -1):
	    mrcam1_drop_rate = line.find(MRCAM1_DROP_RATE_KEYWORD)
	    if (mrcam1_drop_rate != -1):
		value = line[mrcam1_drop_rate+11:]
		MRCAM1_DROP_RATE_LIST.append(value)
	#MRCAM2 drop count
	mrcam2_drop_count = line.find(MRCAM2_DROP_TOTAL_KEYWORD)
	if (mrcam2_drop_count != -1):
	    mrcam2_drop_count_end = line.find(",")
	    value = line[mrcam2_drop_count+23:mrcam2_drop_count_end]
	    MRCAM2_DROP_TOTAL_LIST.append(value)
	#MRCAM2 total count
	mrcam2_total_count = line.find(MRCAM2_TOTAL_KEYWORD)
	if (mrcam2_total_count != -1):
	    value = line[mrcam2_total_count+19:]
	    MRCAM2_TOTAL_LIST.append(value)
	#MRCAM2 drop rate
	mrcam2_drop_count = line.find(MRCAM2_DROP_TOTAL_KEYWORD)
	if (mrcam2_drop_count != -1):
	    mrcam2_drop_rate = line.find(MRCAM2_DROP_RATE_KEYWORD)
	    if (mrcam2_drop_rate != -1):
		value = line[mrcam2_drop_rate+11:]
		MRCAM2_DROP_RATE_LIST.append(value)

    f_log.close()
else:
    print "argument length: " + (str)(argv_len) + " is wrong"
    print "Command example: python " + sys.argv[0] + " main.log"

f_csv = open("main_report.csv", "w+");

#print header
f_csv.write("CPU idle loading")
c = 1
while c <= (len(CPU_IDLE_AVG_ALL_LIST)):
    f_csv.write("," + (str)(c))
    c += 1
f_csv.write("\n")

#print CPU idle loading ALL
f_csv.write("All")
c = 0
while c < (len(CPU_IDLE_AVG_ALL_LIST)):
    f_csv.write("," + (str)(CPU_IDLE_AVG_ALL_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU idle loading Core 0
f_csv.write("Core 0")
c = 0
while c < (len(CPU_IDLE_AVG_CORE_0_LIST)):
    f_csv.write("," + (str)(CPU_IDLE_AVG_CORE_0_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU idle loading Core 1
f_csv.write("Core 1")
c = 0
while c < (len(CPU_IDLE_AVG_CORE_1_LIST)):
    f_csv.write("," + (str)(CPU_IDLE_AVG_CORE_1_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU idle loading Core 2
f_csv.write("Core 2")
c = 0
while c < (len(CPU_IDLE_AVG_CORE_2_LIST)):
    f_csv.write("," + (str)(CPU_IDLE_AVG_CORE_2_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU idle loading Core 3
f_csv.write("Core 3")
c = 0
while c < (len(CPU_IDLE_AVG_CORE_3_LIST)):
    f_csv.write("," + (str)(CPU_IDLE_AVG_CORE_3_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU idle loading Core 4
f_csv.write("Core 4")
c = 0
while c < (len(CPU_IDLE_AVG_CORE_4_LIST)):
    f_csv.write("," + (str)(CPU_IDLE_AVG_CORE_4_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU idle loading Core 5
f_csv.write("Core 5")
c = 0
while c < (len(CPU_IDLE_AVG_CORE_5_LIST)):
    f_csv.write("," + (str)(CPU_IDLE_AVG_CORE_5_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU idle loading Core 6
f_csv.write("Core 6")
c = 0
while c < (len(CPU_IDLE_AVG_CORE_6_LIST)):
    f_csv.write("," + (str)(CPU_IDLE_AVG_CORE_6_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU idle loading Core 7
f_csv.write("Core 7")
c = 0
while c < (len(CPU_IDLE_AVG_CORE_7_LIST)):
    f_csv.write("," + (str)(CPU_IDLE_AVG_CORE_7_LIST[c]))
    c += 1
f_csv.write("\n")

#print separate idle and running
f_csv.write("\n")

#print header
f_csv.write("CPU running loading")
c = 1
while c <= (len(CPU_IDLE_AVG_ALL_LIST)):
    f_csv.write("," + (str)(c))
    c += 1
f_csv.write("\n")

#print CPU running loading ALL
f_csv.write("All")
c = 0
while c < (len(CPU_RUN_AVG_ALL_LIST)):
    f_csv.write("," + (str)(CPU_RUN_AVG_ALL_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU running loading Core 0
f_csv.write("Core 0")
c = 0
while c < (len(CPU_RUN_AVG_CORE_0_LIST)):
    f_csv.write("," + (str)(CPU_RUN_AVG_CORE_0_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU running loading Core 1
f_csv.write("Core 1")
c = 0
while c < (len(CPU_RUN_AVG_CORE_1_LIST)):
    f_csv.write("," + (str)(CPU_RUN_AVG_CORE_1_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU running loading Core 2
f_csv.write("Core 2")
c = 0
while c < (len(CPU_RUN_AVG_CORE_2_LIST)):
    f_csv.write("," + (str)(CPU_RUN_AVG_CORE_2_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU running loading Core 3
f_csv.write("Core 3")
c = 0
while c < (len(CPU_RUN_AVG_CORE_3_LIST)):
    f_csv.write("," + (str)(CPU_RUN_AVG_CORE_3_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU running loading Core 4
f_csv.write("Core 4")
c = 0
while c < (len(CPU_RUN_AVG_CORE_4_LIST)):
    f_csv.write("," + (str)(CPU_RUN_AVG_CORE_4_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU running loading Core 5
f_csv.write("Core 5")
c = 0
while c < (len(CPU_RUN_AVG_CORE_5_LIST)):
    f_csv.write("," + (str)(CPU_RUN_AVG_CORE_5_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU running loading Core 6
f_csv.write("Core 6")
c = 0
while c < (len(CPU_RUN_AVG_CORE_6_LIST)):
    f_csv.write("," + (str)(CPU_RUN_AVG_CORE_6_LIST[c]))
    c += 1
f_csv.write("\n")

#print CPU running loading Core 7
f_csv.write("Core 7")
c = 0
while c < (len(CPU_RUN_AVG_CORE_7_LIST)):
    f_csv.write("," + (str)(CPU_RUN_AVG_CORE_7_LIST[c]))
    c += 1
f_csv.write("\n")

#print separate CPU running and drop rate
f_csv.write("\n")

#print IMU drop count
f_csv.write("IMU drop count")
c = 0
while c < (len(IMU_DROP_TOTAL_LIST)):
    f_csv.write("," + (str)(IMU_DROP_TOTAL_LIST[c]))
    c += 1
f_csv.write("\n")

#print IMU total count
f_csv.write("IMU total count")
c = 0
while c < (len(IMU_TOTAL_LIST)):
    f_csv.write("," + (str)(IMU_TOTAL_LIST[c]))
    c += 1
f_csv.write("\n")

#print IMU drop rate
f_csv.write("IMU drop rate")
c = 0
while c < (len(IMU_DROP_RATE_LIST)):
    f_csv.write("," + (str)(IMU_DROP_RATE_LIST[c]))
    c += 1
f_csv.write("\n")

#print CRA drop count
f_csv.write("CRA drop count")
c = 0
while c < (len(CRA_DROP_TOTAL_LIST)):
    f_csv.write("," + (str)(CRA_DROP_TOTAL_LIST[c]))
    c += 1
f_csv.write("\n")

#print CRA total count
f_csv.write("CRA total count")
c = 0
while c < (len(CRA_TOTAL_LIST)):
    f_csv.write("," + (str)(CRA_TOTAL_LIST[c]))
    c += 1
f_csv.write("\n")

#print CRA drop rate
f_csv.write("CRA drop rate")
c = 0
while c < (len(CRA_DROP_RATE_LIST)):
    f_csv.write("," + (str)(CRA_DROP_RATE_LIST[c]))
    c += 1
f_csv.write("\n")

#print CRB drop count
f_csv.write("CRB drop count")
c = 0
while c < (len(CRB_DROP_TOTAL_LIST)):
    f_csv.write("," + (str)(CRB_DROP_TOTAL_LIST[c]))
    c += 1
f_csv.write("\n")

#print CRB total count
f_csv.write("CRB total count")
c = 0
while c < (len(CRB_TOTAL_LIST)):
    f_csv.write("," + (str)(CRB_TOTAL_LIST[c]))
    c += 1
f_csv.write("\n")

#print CRB drop rate
f_csv.write("CRB drop rate")
c = 0
while c < (len(CRB_DROP_RATE_LIST)):
    f_csv.write("," + (str)(CRB_DROP_RATE_LIST[c]))
    c += 1
f_csv.write("\n")

#print MR Cam1 drop count
f_csv.write("MR Cam1 drop count")
c = 0
while c < (len(MRCAM1_DROP_TOTAL_LIST)):
    f_csv.write("," + (str)(MRCAM1_DROP_TOTAL_LIST[c]))
    c += 1
f_csv.write("\n")

#print MR Cam1 total frame
f_csv.write("MR Cam1 total frame")
c = 0
while c < (len(MRCAM1_TOTAL_LIST)):
    f_csv.write("," + (str)(MRCAM1_TOTAL_LIST[c]))
    c += 1
f_csv.write("\n")

#print MR Cam1 drop rate
f_csv.write("MR Cam1 drop rate")
c = 0
while c < (len(MRCAM1_DROP_RATE_LIST)):
    f_csv.write("," + (str)(MRCAM1_DROP_RATE_LIST[c]))
    c += 1
f_csv.write("\n")

#print MR Cam2 drop count
f_csv.write("MR Cam2 drop count")
c = 0
while c < (len(MRCAM2_DROP_TOTAL_LIST)):
    f_csv.write("," + (str)(MRCAM2_DROP_TOTAL_LIST[c]))
    c += 1
f_csv.write("\n")

#print MR Cam2 total frame
f_csv.write("MR Cam2 total frame")
c = 0
while c < (len(MRCAM2_TOTAL_LIST)):
    f_csv.write("," + (str)(MRCAM2_TOTAL_LIST[c]))
    c += 1
f_csv.write("\n")

#print MR Cam2 drop rate
f_csv.write("MR Cam2 drop rate")
c = 0
while c < (len(MRCAM2_DROP_RATE_LIST)):
    f_csv.write("," + (str)(MRCAM2_DROP_RATE_LIST[c]))
    c += 1
f_csv.write("\n")

f_csv.close()
