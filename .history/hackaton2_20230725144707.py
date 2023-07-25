from tkinter import *       
 
# Following will import tkinter.ttk module and
# automatically override all the widgets
# which are present in tkinter module.
from tkinter.ttk import *
 
# Create Object
root = Tk()
 
# Initialize tkinter window with dimensions 100x100            
root.geometry('100x100')    
 
btn = Button(root, text = 'Click me !',
                command = root.destroy)
root.geometry('150x100')    
 
b = Button(root, text = 'Click me !',
                command = root.destroy)
root.geometry('500x100')    
 
a = Button(root, text = 'Click me !',
                command = root.destroy)
root.geometry('100x100')    
 
c = Button(root, text = 'Click me !',
                command = root.destroy)
 
# Set the position of button on the top of window
btn.place(x=50, y=5, width=200,height=30)
b.place(x=350, y=5, width=200,height=30)
a.place(x=650, y=5, width=200,height=30)
c.place(x=1050, y=5, width=200,height=30)
root.mainloop()