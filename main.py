#import needed dependencies
import os
import fnmatch
import shutil
from pathlib import Path

#assign source-destination folder path
from_folder = r"C:\Users\krayn\test-file-transfering\from"
to_folder = r"C:\Users\krayn\test-file-transfering\to"

# define file patern
pattern = "*txt*"

#sort date from source
paths = sorted(Path(from_folder).iterdir(), key=os.path.getmtime)

# select files that have xml extensions
source_folder = os.listdir(from_folder)

# copy each file from source to destination folder
for file_name in source_folder:
    # if filename match pattern
    if(fnmatch.fnmatch(file_name, pattern)):

        # extract full file name
        full_file_name = os.path.join(from_folder, file_name)

        # if path contains the full filename, move the file from source to destination
        if(os.path.isfile(full_file_name)):
            
            shutil.move(full_file_name, to_folder)

#sort date in destination
paths = sorted(Path(to_folder).iterdir(), key=os.path.getmtime)
