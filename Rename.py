import os
import time

path = input('Please Input the Folder Path: ')

# select all the files in the folder and store them in list
fileList = os.listdir(path)

n = 0

for i in fileList:
    # old name == path + file name
    # os.sep == system based separation sign
    old_name = path + os.sep + fileList[n]

    # setup new file name
    new_name = path + os.sep + 'P' + str(n) + '.jpg'

    # os library rename function
    os.rename(old_name, new_name)

    print(old_name, '==>', new_name)

    n += 1

    time.sleep(1/100)

