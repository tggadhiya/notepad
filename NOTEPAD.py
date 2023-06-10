from tkinter import *
from tkinter import *
top= Tk()
top.geometry("1100x475")
top.title("Notepad")

### text
t=Text(top,width=1000,height=100,font=("Times New Roman ",11))
t.pack()


### 1st

m=Menu(top)
file=Menu(m, tearoff=False)
file.add_command(label="New")
file.add_command(label="New Window")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_command(label="Page Setup....")
file.add_command(label="Print....")
file.add_command(label="Exit")
m.add_cascade(label="File", menu=file)

### 2nd

edit=Menu(m, tearoff=False)
edit.add_command(label="Undo",state=DISABLED)
m.add_cascade(label="Edit", menu=edit)
edit.add_command(label="Cut",state=DISABLED)
edit.add_command(label="Copy",state=DISABLED)
edit.add_command(label="Past")
edit.add_command(label="Delete",state=DISABLED)
edit.add_command(label="Search With Bing....",state=DISABLED)
edit.add_command(label="Find....",state=DISABLED)
edit.add_command(label="Find Next",state=DISABLED)
edit.add_command(label="Find Previous",state=DISABLED)
edit.add_command(label="Replace....")
edit.add_command(label="Go To....")
edit.add_command(label="Select All")
edit.add_command(label="Time / Date")
top.config(menu=m)

### 3rd

fem=Menu(m, tearoff=False)
fem.add_command(label="Word Wrap")
m.add_cascade(label="Formet", menu=fem)
fem.add_command(label="Font....")
top.config(menu=m)


### 4th

vie=Menu(m, tearoff=False)
vie.add_command(label="Zoom")
m.add_cascade(label="View", menu=vie)
vie.add_command(label="Status Bar")
top.config(menu=m)

### 5th

hel=Menu(m, tearoff=False)
hel.add_command(label="View Help")
m.add_cascade(label="Help", menu=hel)
hel.add_command(label="Send Feedback")
hel.add_command(label="About Notepad")
top.config(menu=m)


top.mainloop()




