"""
Watches a folder and prints out filenames as files are modified, added or removed.

ARGS: Path to watch. Drag and drop from finder.
"""
import sys
import os
import time

beep = True #change to not beep on each file change
path = sys.argv[1]
change_total = -1 #number of file changes to beep on
count = 0 #total number of files changed since execution start
try:
    change_total = int(sys.argv[2])
except IndexError:
    pass

#Gets list of all filepaths in given directory
#ARGS: Str - Directory path
#RETURNS: List[Str] - List of filepaths
def get_filepath_list(path):
    filepath_list = []
    file_list = os.listdir(path)
    #get full path for each file
    for filename in file_list:
        filepath_list.append(path + '/' + filename)
    return filepath_list

#Checks to see if filepath is a system file
#ARGS: Str - Filepath
#RETURNS: Bool 
def system_file(filepath):
    last_slash_index = filepath.rfind('/')
    if filepath[last_slash_index + 1] == '.':
        return True
    return False

file_dict = {}
filepath_list = get_filepath_list(path)

#create dict associating filepath and last change time
for file in filepath_list:
    if not system_file(file):
        file_dict[file] = os.stat(file)[9]

#check for changes every 10 seconds. Print out changed or new files. Ctr-c to exit.
while(True):
    time.sleep(10) #In seconds, change for longer or shorter check cycle.
    new_file_dict = {}
    changes = False
    for file in get_filepath_list(path):
        if system_file(file):
            continue  #ignore system files
        new_file_dict[file] = os.stat(file)[9] #create new dict with last change time
    for file in file_dict:
        try:
            if file_dict[file] != new_file_dict[file]:
                count += 1
                print(str(count) + '- File changed: ' + file) #check for changes, print file if different 
                changes = True
                if beep:
                    print('\a')
        except KeyError: #check for deleted files, print file if deleted
            print('File removed : ' + file)
            changes = True
    for file in new_file_dict:
        if file not in file_dict.keys():
            count += 1
            print(str(count) + '- New file : ' + file) #check for new files, print file if new
            changes = True
            if beep:
                    print('\a')
    if changes: 
        file_dict = new_file_dict
    if change_total == count: 
        print('\a')
        print('\a')
        print('\a')
        change_total = -1
        #beep if total changed files reach stated total.
        #Ignores deleted files, counts new and changed.
