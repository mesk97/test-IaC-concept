# Task:
#   1. read all processes
#   2. write PID, cmdline, heap address  
# mesk@BG-PF2WX41J:~$ sudo cat /proc/1/maps
# 00200000-00225000 r--p 00000000 00:15 281474977649925                    /init
# 00225000-00294000 r-xp 00025000 00:15 281474977649925                    /init
# 00294000-0029b000 rw-p 00094000 00:15 281474977649925                    /init
# 0029b000-002a1000 rw-p 00000000 00:00 0
# 00a08000-00a11000 rw-p 00000000 00:00 0                                  [heap]
# 7fc45b898000-7fc45b899000 ---p 00000000 00:00 0
# 7fc45b899000-7fc45b8ae000 rw-p 00000000 00:00 0
# 7ffd5b5e6000-7ffd5b607000 rw-p 00000000 00:00 0                          [stack]
# 7ffd5b74d000-7ffd5b751000 r--p 00000000 00:00 0                          [vvar]
# 7ffd5b751000-7ffd5b752000 r-xp 00000000 00:00 0                          [vdso]
# mesk@BG-PF2WX41J:~$

import sys
import subprocess
import os

def get_process_list():
    processes = []

    for e in os.listdir("/proc/"):
        if str(e).isnumeric():
            processes.append(int(e))
    return processes

def get_info(pid):
    info = [pid]

    # read maps
    with open("/proc/%d/maps" % (pid)) as file:
        for line in file:
            slice = line.split()
            if slice[-1] == "[heap]":
                info.append(slice[0])
    
    # read cmdline
    result = subprocess.run(['cat', "/proc/%d/cmdline" % (pid)], stdout=subprocess.PIPE)
    info.append(str(result.stdout))
    
    return info

def main():
    for pid in get_process_list():
        print(str(get_info(pid)))
    return 

if __name__ == "__main__":
    main()