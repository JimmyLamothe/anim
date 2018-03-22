#Returns a file path from the file_dialog
import tkinter
from tkinter.filedialog import askopenfilename

def get_path():
    root = tkinter.Tk()
    root.withdraw()
    filepath = askopenfilename()
    return filepath

