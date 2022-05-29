import os
import time
import shutil

path = input('Enter folder path: ')
timeLimit = time.time() - 25*86400
for i in os.listdir(dir_path):
    if os.path.getmtime(path) > 0:
            os.remove(path)
            print('file deleted')