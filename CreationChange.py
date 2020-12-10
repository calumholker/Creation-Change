from subprocess import call
import os
from datetime import datetime

def space_invader(dir):
    restart = 0
    for file in os.listdir(dir):
        fullPath = os.path.join(dir, file)
        if ' ' in fullPath:
            os.rename(fullPath, fullPath.replace(' ', '_'))
            restart = 1
            break
        elif ';' in fullPath:
            os.rename(fullPath, fullPath.replace(';', '_'))
            restart = 1
            break
        elif os.path.isdir(fullPath):
            space_invader(fullPath)
    if restart == 1:
        space_invader(dir)

def exorcist(fullPath):
    filename = (os.path.basename(fullPath))[0:24]
    format = 'clip-%Y-%m-%d_%H_%M_%S'
    date_time = datetime.strptime(filename, format)
    return date_time

directory = input("enter dir:")
space_invader(directory)

for subdir, dirs, files in os.walk(directory):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".dv") or filepath.endswith(".mov"):
            try:
                new_date = exorcist(filepath)
                os.system('SetFile -d "{}" {}'.format(new_date.strftime('%m/%d/%Y %H:%M:%S'), filepath))
            except:
                if 'Cache' not in filepath:
                    print("UNORTHADOX FILE NAME DETECTED: " + filepath)