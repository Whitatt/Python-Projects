import tkinter as tk
from tkinter import filedialog

root=tk.Tk()

#setting windows size

root.geometry("600x400")

#declaring string variable
#for storing source/destination folder

source_var=tk.StringVar()
destination_var=tk.StringVar()

def ChooseSource():
    src = filedialog.askdirectory()
    

def submit():#defining a function that will get source/dest and print on screen

    source=source_var.get()
    destination=destination_var.get()

    print("The source is : " + source)
    print("The destination is : " + destination)

    source_var.set()
    destination_var.set()

source_label = tk.Label(root, text = 'Source', font=('calibre',10, 'bold'))#creating label for source 

source_entry = tk.Entry(root,textvariable = source_var, font=('calibre',10,'normal'))#creating label for entry

destination_label = tk.Label(root, text = 'Destination', font = ('calibre',10,'bold'))
  
destination_entry=tk.Entry(root, textvariable = destination_var, font = ('calibre',10,'normal'), show = '*')

sub_btn=tk.Button(root,text = 'Select Source', command = submit)#creating button widget
sub_btn1=tk.Button(root,text = 'Select Destination', command = submit)
sub_btn2=tk.Button(root,text = 'Select Transfer', command = submit)
        





source_label.grid(row=0,column=0)#creating label and entry using grid methos
source_entry.grid(row=0,column=1)
destination_label.grid(row=1,column=0)
destination_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
sub_btn1.grid(row=3,column=1)
sub_btn2.grid(row=4,column=1)


root.mainloop()#infinite loop for window to display

    


