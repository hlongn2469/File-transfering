  
#import needed dependencies
from genericpath import getmtime
import os
import fnmatch
import shutil
from pathlib import Path
import glob
import time

def transferFile():
    # define file patern
    pattern = "*txt*"

    files = glob.glob(os.path.expanduser(from_folder_files))
    sorted_by_mtime_ascending = sorted(files, key=lambda t: os.stat(t).st_mtime)

    count = 0
    global_time = 0
    list = []
    # move file
    for file in sorted_by_mtime_ascending:
        # if filename match pattern
        if(fnmatch.fnmatch(file, pattern)):
            # extract full file name
            full_file_name = os.path.join(source_folder, file)
            if(count == 0):
                global_time = os.path.getmtime(full_file_name)
                if(os.path.isfile(full_file_name)):
                    print(full_file_name)
                    list.append(full_file_name)
                    
            else:
                thresh_hold = os.path.getmtime(full_file_name)
                print("global time: " + time.ctime(global_time))
                print("thresh hold time: " + time.ctime(thresh_hold))
                if(global_time == thresh_hold):
                    print(global_time)
                    print(thresh_hold)
                    print("same modified date detected")
                    # if path contains the full filename, move the file from source to destination
                    if(os.path.isfile(full_file_name)):
                        print(full_file_name)
                        list.append(full_file_name)
                        
                else: 
                    break   
            
        count +=1
    
    return_count = 0
    for item in list:
        return_count +=1
        shutil.move(item, to_folder)

    return return_count


# select files that have xml extensions
#assign source-destination folder path
from_folder_files = r"C:\Users\krayn\test-file-transfering\From\*"
source_folder = r"C:\Users\krayn\test-file-transfering\From"
to_folder = r"C:\Users\krayn\test-file-transfering\To4"
source_f = os.listdir(source_folder)
to_f = os.listdir(to_folder)

len_source = len(source_f)
len_dest = len(to_f)
while(len_dest == 0):
    print(len_source)
    print(len_dest)
    len_deduct = transferFile()
    len_source-=len_deduct
    len_dest+=len_deduct
    
    
    


        
