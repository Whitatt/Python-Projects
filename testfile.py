# Import required python modules
from tkinter import *
import tkinter as tk

# Import custom module identifiers
import testfunc
import testmain


def load_gui(self):
    self.src_lbl = tk.Label(
        self.master,
        font=("Helvetica", 16),
        fg="#fff",
        bg="#333",
        text="Choose Source Directory",
    )
    self.src_lbl.grid(row=0, column=0, padx=(160, 0), pady=(50, 0), sticky=NSEW)
    self.src_lbl.grid_rowconfigure(0, weight=1)

    self.src_ent = tk.Entry(self.master, width=40)
    self.src_ent.grid(row=1, column=0, padx=(160, 0), pady=(5, 0), sticky=NSEW)
    self.src_ent.grid_rowconfigure(0, weight=1)

    self.src_btn = tk.Button(
        self.master,
        highlightbackground="#333",
        text="Browse",
        command=lambda: testfunc.src_dir(self),
    )
    self.src_btn.grid(row=2, column=0, padx=(160, 0), pady=(10, 0), sticky=NSEW)
    self.src_btn.grid_rowconfigure(0, weight=1)

    self.dest_lbl = tk.Label(
        self.master,
        font=("Helvetica", 16),
        fg="#fff",
        bg="#333",
        text="Choose Destination Directory",
    )
    self.dest_lbl.grid(row=3, column=0, padx=(160, 0), pady=(50, 0), sticky=NSEW)
    self.dest_lbl.grid_rowconfigure(0, weight=1)

    self.dest_ent = tk.Entry(self.master, width=40)
    self.dest_ent.grid(row=4, column=0, padx=(160, 0), pady=(5, 0), sticky=NSEW)
    self.dest_ent.grid_rowconfigure(0, weight=1)

    self.dest_btn = tk.Button(
        self.master,
        highlightbackground="#333",
        text="Browse",
        command=lambda: testfunc.dest_dir(self),
    )
    self.dest_btn.grid(row=5, column=0, padx=(160, 0), pady=(10, 0), sticky=NSEW)
    self.dest_btn.grid_rowconfigure(0, weight=1)


if __name__ == "__main__":
    pass
