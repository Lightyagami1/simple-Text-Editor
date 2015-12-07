from tkinter import *
import tkinter.filedialog as tkfd
import tkinter.scrolledtext as tkst

filename = ''

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def openFile():
    filename = tkfd.askopenfilename (initialdir = "$HOME", title = "choose your file", filetypes = (("text file",".txt"),("all files","*.*"))) in globals()
    fileInstance = open(filename, 'r+')
    text.insert("end", fileInstance.read())
    fileInstance.close()

def saveFile():
    fileInstance = open(filename, 'r+')
    fileInstance.write(text.get(1.0, END))
    fileInstance.close()

def about():
    label = Label(root, text="Made by Master Saurav Kumar, started on 29 th November 2015")
    label.pack()

def exit():
    root.quit()

root = Tk()

root.title ("TextEditorsKaBaap")

menuFrame = Frame (root)
menuFrame.pack(side = TOP)
textFrame = Frame(root)
textFrame.pack (side = BOTTOM, expand="yes")
text = tkst.ScrolledText(textFrame)
text.pack(expand=True)
text.insert(END, "")


menubar = Menu(menuFrame)
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

