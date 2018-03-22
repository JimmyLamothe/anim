#WORK IN PROGRESS
import os
import sys
import time
import tkinter
from file_dialog import get_path
from tkinter.filedialog import askopenfilename


test = True

filepath = get_path()
print(filepath)

time.sleep(1)

max = 10
current = 0

while True:
    print(filepath)
    current += 1
    if current >= max:
        break
    time.sleep(1)


if test:
    sys.exit(0)

