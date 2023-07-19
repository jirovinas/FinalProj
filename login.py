# from tkinter import *
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from PIL import Image, ImageTk

# root = tk.Tk()
# root.geometry("475x265")
# root.title("Login Interface") 
# #root.resizable(False, False)

# path = "H.jpg"
# bg = ImageTk.PhotoImage(file = path)
# my_canva = Canvas(root, height=265, width=475)
# my_canva.pack(fill="both")

# my_canva.create_image(0,0,image=bg, anchor="nw")

# my_canva.create_text(250, 20, text="Sign In", font=("Arial", 20),fill="black")
# # my_canva.create_text(70, 80, text="Username:", font=("Arial", 20),fill="white")
# # my_canva.create_text(70, 130, text="Password:", font=("Arial", 20),fill="white")


# userLabel = LabelFrame(root, text="Username", width=15)
# username = Entry(userLabel,font=("Arial", 18))
# username.pack()
# username_w = my_canva.create_window(110, 60, anchor="nw", window=userLabel)

# passwordLabel = LabelFrame(root, text="Password", width=15)
# password = Entry(passwordLabel,font=("Arial", 18))
# password.pack()
# password_w = my_canva.create_window(110, 110, anchor="nw", window=passwordLabel)

# button1 = Button(root, text="Login", width=20, bg="lightblue")
# button1_window = my_canva.create_window(170, 170, anchor="nw", window=button1)


# tk.mainloop()
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("475x265")
root.title("Login Interface") 
#root.resizable(False, False)

path = "pic.jpg"
bg = ImageTk.PhotoImage(file = path)
my_canva = Canvas(root, height=265, width=475)
my_canva.pack(fill="both")

my_canva.create_image(0,0,image=bg, anchor="nw")

my_canva.create_text(250, 20, text="Sign In", font=("Arial", 20),fill="black")

userLabel = LabelFrame(root, text="Username", width=15, bg="white")
username = Entry(userLabel,font=("Arial", 18))
username.pack()
username_w = my_canva.create_window(110, 60, anchor="nw", window=userLabel)

passwordLabel = LabelFrame(root, text="Password", width=15)
password = Entry(passwordLabel,font=("Arial", 18))
password.pack()
password_w = my_canva.create_window(110, 110, anchor="nw", window=passwordLabel)

button1 = Button(root, text="Login", width=20, bg="lightblue")
button1_window = my_canva.create_window(170, 170, anchor="nw", window=button1)


tk.mainloop()
