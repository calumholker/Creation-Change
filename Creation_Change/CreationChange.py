from subprocess import call
import os
from datetime import datetime

def exorcist(fullPath):
    filename = (os.path.basename(fullPath))[0:24]
    format = 'clip-%Y-%m-%d_%H_%M_%S'
    date_time = datetime.strptime(filename, format)
    return date_time

directory = input("enter dir:")

for subdir, dirs, files in os.walk(directory):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".dv") or filepath.endswith(".mov"):
            try:
                new_date = exorcist(filepath)
                command = 'Touch -t ' + new_date.strftime('%Y%m%d%H%M.%S') + ' "' + filepath + '"'
                call(command, shell=True)
            except:
                if 'Cache' not in filepath:
                    print("UNORTHADOX FILE NAME DETECTED: " + filepath)