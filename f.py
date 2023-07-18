from  tkinter import *
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
from openpyxl import *
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from PIL import Image, ImageTk
import os 

root = tk.Tk()
root.geometry("1050x600")
root.title("Login Interface")


file = "Sample_file.xlsx"
sheetDefault = "default"
sheetNew = "newData"

if os.path.exists(file):
    excel_con = load_workbook(file)
    excel_active = excel_con[sheetDefault]
else:
	excel_con = Workbook()
	excel_active = excel_con.active
	excel_active.title = sheetDefault

excel_con.create_sheet(sheetNew)

excel_con.save(file)

topframe = Frame(root, height=50, width=1050, bg="black")
topframe.pack(fill="x", side="top")
leftframe = Frame(root, height=600, width=200, bg="black", bd=0)
leftframe.pack(fill="y",side='left')
rigthframe = Frame(root, height=600, width=750)
rigthframe.pack(fill="both", side='right')

l = Label(topframe,text="Dalubhasaan Ng Lungsod Ng Lucena", bg="black", fg="white", font=("Arial", 30))
l.pack()
gender_var = StringVar()


b = (Image.open("dll_logo.png"))
resized_image = b.resize((150, 150))
new_image = ImageTk.PhotoImage(resized_image)
# canva = Canvas(leftframe, height=150, width=150, relief=None)
# canva.place(x=30, y=50)
# canva.create_image(0,0,image=new_image, anchor="nw")
Label(leftframe, image=new_image, bg="black").pack()

rFrame = Frame(leftframe)
gender_var.set("Old")
old_R = Radiobutton(rFrame, text="Old", variable=gender_var, value="Old")
new_R = Radiobutton(rFrame, text="New", variable=gender_var, value="New")
# old_R.place(x=30, y=250)
# new_R.place(x=130, y=250)

old_R.pack(side='left')
new_R.pack(side='left')

rFrame.pack()

butFrame = Frame(leftframe)

rb = Button(butFrame, text="Register", width=10)
lb = Button(butFrame, text="Login", width=10)
# rb.place(x=10, y=300)
# lb.place(x=120, y=300)

rb.pack(side='left')
lb.pack(side='left')

butFrame.pack()

def showProf():
	prof.pack(fill="both")
	abt.pack_forget()

def showAbt():
	abt.pack(fill="both")
	prof.pack_forget()

abt_b = Button(topframe, text="About", command=showAbt, font=("Arial",15), bg="black", fg="white", bd=0)
abt_b.pack(side=RIGHT, anchor=N)
prof_b = Button(topframe, text="Profile", command=showProf, font=("Arial",15), bg="black", fg="white", bd=0)
prof_b.pack(side=RIGHT, anchor=N)

prof = Frame(rigthframe, bg="black")

bg = (Image.open("school.jpg"))
resized_imag = bg.resize((1050, 600))
new_imag = ImageTk.PhotoImage(resized_imag)
my_canva = Canvas(prof, height=600, width=1050)
my_canva.pack()
my_canva.create_image(0,0,image=new_imag, anchor="nw")
prof.pack()

abt = Frame(rigthframe, width=600, height=750)
abt_l = Label(abt,text=f"Dalubhasaan ng Lungsod ng Lucena"
"\nOne of the high impact programs of Mayor Roderick A. Alcala is free quality tertiary education."
"\nWhen he assumed office in 2012, Dalubhasaan ng Lungsod ng Lucena (DLL),"
"\n was his vision of providing access to college education for free."
"\nMayor Alcala envisions DLL as an institution that would provide easy access to higher education and," 
"\nultimately develop the competencies of the youth of the city to meet the demands of the local industries and businesses."
"\nThrough DLL, students from low-income families are able to enrol in degree programs at no cost."
"\nThe annual appropriation of the local government has allowed DLL to cover all its operation expenses,"
"\nincluding tuition and miscellaneous fees of students."
"\nThe college, operated, managed, and fully-subsidized by the City Government, implements a zero-collection policy."
"\nAt present, DLL has a total of nine degree programs and continue to apply for additional academic programs to accommodate more scholars:"
"\nBachelor of Arts in Information Technology"
"\nBachelor of Arts in Public Administration"
"\nBachelor of Science in Accountancy"
"\nBachelor of Science in Accounting Information System"
"\nBachelor of Science in English Language Studies"
"\nBachelor of Science in Entrepreneurship"
"\nBachelor of Science in Social Work"
"\nBachelor in Technical Vocational Teacher’s Education"
"\nDiploma in Hotel and Restaurant Services"
"\nAt present the former annex building of Lucena City Hall is being renovated to accommodate the growing student population of DLL.", justify="center", font=("Arial", 10))
abt.pack()
abt_l.pack()

showProf()


root.mainloop()

