import webbrowser
from tkinter import *
import tkinter as tk

def load_gui(self):

    self.entry1=tk.Entry(self.master)
    self.entry1.grid(row=0,column=0)
    self.txt_button=tk.Button(self.master,width=20,height=2,text='Open HTML file')
    self.txt_button.grid(row=1,column=0)
        


    def Submit(self):
        txt=self.entry1.get()
        f = open(webbrowser)

        message = """
        <html>
            <body>
                <h1>"""+txt+"""</h1>
            </body>
        </html>"""
        
        f.write(message)
        f.close()
        webbrowser.open_new_tab('')
        


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        load_gui(self)

    


if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
