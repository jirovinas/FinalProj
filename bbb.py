from http.client import FOUND
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from openpyxl import *
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from PIL import Image, ImageTk

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.pack()

canvas_text = canvas.create_text(10, 10, text='', anchor=tk.NW)

test_string = "fgdgdgdgfdgfdgfdgfdgdfgfdgdgfdgfdgfdfg"
#Time delay between chars, in milliseconds
delta = 100 
delay = 0
for i in range(len(test_string) + 1):
    s = test_string[:i]
    update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
    canvas.after(delay, update_text)
    delay += delta

root.mainloop()