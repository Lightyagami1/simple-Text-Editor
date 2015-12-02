from tkinter import *


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def openFile():
    fileInstance = open(filename.GetValue(), 'w')
    contents.SetValue(file.read())
    file.close()

def saveFile(event):
    fileInstance = open(filename.GetValue(), 'w')
    fileInstance.write(contents.GetValue())
    fileInstance.close()

def about():
    label = Label(root, text="Made by Master Saurav Kumar, started on 29 th November 2015")
    label.pack()

def exit():
    root.quit()

root = Tk()
text = Text(root)
text.insert(END, ".....hello")
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_command(label="Exit", command=exit)

menubar.add_cascade(label="File", menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

#editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
text.pack()
text.tag_config("here", background="yellow", foreground = "blue")
root.mainloop()

