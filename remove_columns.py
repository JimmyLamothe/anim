#Removes unwanted + duplicate info from SBPro csv export.
import csv
import sys
from anim_utilities import episode_format

episode_number = 0

try:
    episode_number = int(input('Which Episode?\n'))
except ValueError:
    print('Invalid Entry')
    sys.exit(0)

episode = episode_format(episode_number)

dir = '/Users/jimmy/Desktop/GENIUS/EXPORTS/'

dir2 = 'EP' + episode[1:] + '/'

base = 'Liste_longueurs_sc_'

old = '_source'

extension = '.csv'

filename = dir + dir2 + base + episode + old + extension
new_filename = dir + dir2 + base + episode + extension
headers = ['Numéro de scène',"Nombre d'images"]

print(filename)
print(new_filename)
with open(filename, newline='') as scene_list:
    with open(new_filename, 'w', newline='', encoding='utf-16') as output_file:
        reader = csv.reader(scene_list)
        writer = csv.writer(output_file)
        writer.writerow(headers)
        prev_scene = ""
        for row in reader:
            if row[1] != prev_scene:
                new_row = [row[1],row[2]]
                print(row)
                print(new_row)
                writer.writerow(new_row)
                prev_scene = row[1]

"""
with open(filename + '_JM', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
"""
