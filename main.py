from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk

# Defining TextEditor Class
class TextEditor:
  # Defining Constructor
  def __init__(self,root):
    self.fontSize=20
# creating  the window.
    self.root = root
    self.root.title("TEXT EDITOR")
    self.root.geometry("600x550")
    # Initializing filename
    self.filename = None
    self.title = StringVar()
    self.status = StringVar()
    # Creating Titlebar
    self.titlebar = Label(self.root,textvariable=self.title,font=("times new roman",18,"bold"),bd=2,relief=GROOVE)
    self.titlebar.pack(side=TOP,fill=BOTH)
    self.settitle()

    # Creating Statusbar
    self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",18,"bold"),bd=2,relief=GROOVE)
    self.statusbar.pack(side=BOTTOM,fill=BOTH)
    self.status.set("Welcome To Text Editor")

    # Creating Menubar
    self.menubar = Menu(self.root,font=("Liberation Mono",80,"italic"),activebackground="#FFFFFF")
    self.root.config(menu=self.menubar)

    # Creating File Menu
    self.filemenu = Menu(self.menubar,font=("Liberation Mono",10,"roman"),activebackground="#000000",tearoff=0)
    self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
    self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
    self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
    self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)


    # Adding Seprator
    self.filemenu.add_separator()
    self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
    self.menubar.add_cascade(label="File", menu=self.filemenu)

    # Creating Edit Menu
    self.editmenu = Menu(self.menubar,font=("Liberation Mono",10,"roman"),activebackground="#000000",tearoff=0)
    self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
    self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
    self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
    # Cascading editmenu to menubar
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)



	 # Creating Font size
    self.Font = Menu(self.menubar,font=("Liberation Mono",10,"roman"),activebackground="#000000",tearoff=0)
    self.Font.add_command(label="size Up",accelerator="A+",command=self.up)
    self.Font.add_command(label="size Down",accelerator="A-",command=self.down)
    self.Font.add_command(label="Bold ",accelerator="𝗔",command=self.bold)
    self.Font.add_command(label="italic ",accelerator="𝘈",command=self.itali)
    self.menubar.add_cascade(label="Font size", menu=self.Font)

		 # Creating Font color
    self.Font_color = Menu(self.menubar,font=("Liberation Mono",10,"roman"),tearoff=0)
    self.Font_color.add_command(label="red",command=self.Red ,activebackground="#EE5566")#,command=self.function_name
    self.Font_color.add_command(label="black",command=self.black ,activebackground="black")#,command=self.function_name
    self.Font_color.add_command(label="Blue ",command=self.blue,activebackground="blue")#,command=self.function_name
    self.Font_color.add_command(label="Yellow ",command=self.yellow,activebackground="yellow")#,command=self.function_name
    self.menubar.add_cascade(label="Font color", menu=self.Font_color)

     # Creating layout 
    self.lay = Menu(self.menubar,font=("Liberation Mono",10,"roman"),activebackground="#000000",tearoff=0)
    self.lay.add_command(label="Dark Mode",command=self.DarkMode)#,command=self.function_name
    self.lay.add_command(label="lite Mode",command=self.Mode)#,command=self.function_name
    self.menubar.add_cascade(label="layout", menu=self.lay)

    # Creating Help Menu
    self.helpmenu = Menu(self.menubar,font=("Liberation Mono",10,"roman"),activebackground="#000000",tearoff=0)
    self.helpmenu.add_command(label="About",command=self.infoabout)
    self.menubar.add_cascade(label="Help", menu=self.helpmenu)


    # Creating Scrollbar
    scrol_y = Scrollbar(self.root,orient=VERTICAL)
    # Creating Text Area
    self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",self.fontSize,"normal"),state="normal",relief=GROOVE)
    # Packing scrollbar to root window
    scrol_y.pack(side=RIGHT,fill=Y)
    # Adding Scrollbar to text area
    scrol_y.config(command=self.txtarea.yview)
    # Packing Text Area to root window
    self.txtarea.pack(fill=BOTH,expand=1)
    self.shortcuts()   

  

  # Defining settitle function
  def settitle(self):
    # Checking if Filename is not None
    if self.filename:
      # Updating Title as filename
      self.title.set(self.filename)
    else:
      # Updating Title as Untitled
      self.title.set("Untitled")


  # Defining New file Function
  def newfile(self,*args):
    self.txtarea.delete("1.0",END)
    self.filename = None
    self.settitle()
    # updating status
    self.status.set("New File Created")


  # Defining Open File Funtion
  def openfile(self,*args):
    # Exception handling
    try:
      # Asking for file to open
      self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      if self.filename:
        infile = open(self.filename,"r")
        # Clearing text area
        self.txtarea.delete("1.0",END)
        for line in infile:
          self.txtarea.insert(END,line)
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Opened Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)


  # Defining Save File Funtion
  def savefile(self,*args):
    # Exception handling
    try:
      if self.filename:
        # Reading the data from text area
        data = self.txtarea.get("1.0",END)
        outfile = open(self.filename,"w")
        outfile.write(data)
        outfile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Saved Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  def saveasfile(self,*args):
          # Exception handling
          try:
            # Asking for file name and type to save
            untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
            # Reading the data from text area
            data = self.txtarea.get("1.0",END)
            # opening File in write mode
            outfile = open(untitledfile,"w")
            outfile.write(data)
            outfile.close()
            # Updating filename as Untitled
            self.filename = untitledfile
            # Calling Set title
            self.settitle()
            # Updating Status
            self.status.set("Saved Successfully")
          except Exception as e:
            messagebox.showerror("Exception",e)
  
  def exit(self,*args):
    op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
    if op>0:
      self.root.destroy()
    else:
      return
      
  # Defining Cut Funtion
  def cut(self,*args):
    self.txtarea.event_generate("<<Cut>>")
  # Defining Copy Funtion
  def copy(self,*args):
          self.txtarea.event_generate("<<Copy>>")
  # Defining Paste Funtion
  def paste(self,*args):
    self.txtarea.event_generate("<<Paste>>")
  # Defining Undo Funtion
  def undo(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # opening File in read mode
        infile = open(self.filename,"r")
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing File
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
      else:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # Updating filename as None
        self.filename = None
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

#add function of fonts color
  def black (self):
    self.txtarea.configure(fg='black')

  def blue (self):
    self.txtarea.configure(fg='blue')

  def yellow (self):
    self.txtarea.configure(fg='yellow')
    
  def Red (self):
    self.txtarea.configure(fg='red') 

  #add function of fonts _size
  def up (self):
    self.fontSize+=2
    self.txtarea.configure(font=("times new roman",self.fontSize,"normal"))

  def down (self):
    self.fontSize-=2
    self.txtarea.configure(font=("times new roman",self.fontSize,"normal"))    

  def bold (self):
    self.txtarea.configure(font=("times new roman",self.fontSize,"bold italic"))

  def itali (self):
    self.txtarea.configure(font=("times new roman",self.fontSize,"italic"))

      #add function of layout
  def DarkMode (self):
    self.txtarea.configure(bg='black',fg='white')

  def Mode (self):
    self.txtarea.configure(bg='#FFFAFF',fg='black')


  # Defining About Funtion
  def infoabout(self):
    messagebox.showinfo("About Text Editor","A Simple Text Editor\nCreated using Python.")
  # Defining shortcuts Funtion
  def shortcuts(self):
    self.txtarea.bind("<Control-n>",self.newfile)
    self.txtarea.bind("<Control-o>",self.openfile)
    self.txtarea.bind("<Control-s>",self.savefile)
    self.txtarea.bind("<Control-a>",self.saveasfile)
    self.txtarea.bind("<Control-e>",self.exit)
    self.txtarea.bind("<Control-x>",self.cut)
    self.txtarea.bind("<Control-c>",self.copy)
    self.txtarea.bind("<Control-v>",self.paste)
    self.txtarea.bind("<Control-u>",self.undo)

root = Tk()
TextEditor(root)
root.mainloop()