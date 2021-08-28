# Python Ver: 3.9.6
#
# Author:       Matthew White
#
# Purpose:      Phonebook Demo. Demonstrating OOP, TKinter GUI module,
#               using TKinter Parent and Child relationships.
#
# Tested OS:    This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk


# Be sure to import our other modules
# so we can have access to them
import drill50_phonebook_gui
import drill50_phonebook_func



# Frame is the TKinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)
        # This CenterWindow method will center our app on the user's screen
        drill_50_phonebook_func.center_window(self,500,300)
        self.master.title("The TKinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master







if __name__ == "__main__":
    root = tk.TK()
    App = ParentWindow(root)
    root.mainloop()
        
