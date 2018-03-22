#Renames sound files for Genius Genie to have them listed by line number.

import os, sys, shutil

episode = input('Which episode\n')

base = '/YY2_0'

base2 = '/YY2_Ep0'

#add 0 for first 9 episodes
if len(episode) == 1:
    base += '0'
    base2 += '0'

#remove 0 for episodes 100 + up
if len(episode) == 3:
    base = base[:-1]
    base2 = base2[:-1]

basepath = "/Users/jimmy/Desktop/YAYA/Enregistrements"

dir1 = base + episode

dir2 = base2 + episode + '_SPLIT LINES'

newdir2 = base2 + episode + '_BY LINE NUMBER'

fullpath = basepath + dir1 + dir2

newpath = basepath + dir1 + newdir2

#create new path
try:
    os.mkdir(newpath)

except FileExistsError:
    print('directory already exists\n')
    #sys.exit(0)

#change filename order
for filename in os.listdir(fullpath):
    if filename[0] == '.':
        continue
    #find underscores
    underscore_index = [pos for pos, char in enumerate(filename) if char == '_']
    #find extension
    point_index = [pos for pos, char in enumerate(filename) if char == '.']
    start = filename[:underscore_index[1]]
    character = filename[underscore_index[-2]:underscore_index[-1]]
    line_number = filename[underscore_index[-1]:point_index[0]]
    #check for non-standard formatting
    try:
        if line_number[1] != 'L':
            line_number = '_L' + line_number[1:]

    except IndexError:
    #if all else fails copy file with no change and warn
        print('WARNING: check this filename manually: ' + filename + '\n')
        shutil.copy2(fullpath + '/' + filename, newpath + '/' + filename)
        continue
    #check for non-standard line numbers
    try:
        int(line_number[-1:])
    except ValueError:
        print('Warning: check this filename manually: ' + filename + '\n')
    #add 0 for first 9 lines
    if len(line_number) == 3:
        line_number = line_number[0:2] + "0" + line_number[2:]
    extension = filename[point_index[0]:]
    new_filename = start + line_number + character + extension
    #copy files to new directory with new name
    shutil.copy2(fullpath + '/' + filename, newpath + '/' + new_filename)
    
