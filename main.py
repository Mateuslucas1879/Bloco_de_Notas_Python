from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("Bloco_de_Notas")
    file = None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file = asksaveasfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " -Bloco_de_Notas")
        TextArea.delete(1.0,END)
        f =open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == "":
            file = None
        else:
            f = open(file,"u")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+ "-Bloco_de_Notas")
            print("File Saved")
    else:
        f =open(file,"u")
        f.write(TextArea.get(1.0,END))
        f.close()


def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<>"))
def copy():
    TextArea.event_generate(("<>"))
def paste():
    TextArea.event_generate(("<>"))
def about():
    showinfo("Bloco_de_Notas","Bloco_de_Notas Codado por Mateus_Lucas")

if __name__ == '__main__':
    root = Tk()
    root.title("Bloco_de_Notas")
    root.geometry("644x788")
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True,fill=BOTH)


    MenuBar = Menu(root)
    root.config(menu=MenuBar)


    fileMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New", command=newfile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=savefile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quitApp)


    editMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)


    helpMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="Help", menu=helpMenu)
    helpMenu.add_command(label="About", command=about)



    root.mainloop()



