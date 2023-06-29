import tkinter as tk
from check_file import select_file

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Audio from Video")
        self.root.geometry('150x100')

    def run(self):
        self.create_button()
        self.root.mainloop()

    def create_button(self):
        tk.Button(self.root, text="Select file", command=select_file).pack()
