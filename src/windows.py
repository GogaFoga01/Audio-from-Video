import time
import tkinter as tk
from tkinter.ttk import Progressbar
from time import sleep

from check_file import select_file


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Audio from Video")
        self.root.geometry('350x300')

    def run(self):
        self.create_button()
        # self.progress()
        self.root.mainloop()

    def progress(self):
        self.pb = Progressbar(self.root, orient="horizontal", mode="determinate", length=100)
        self.pb.pack()

        for i in range(101):
            self.pb.configure(value=i)
            self.pb.update()
            sleep(0.05)

    def create_button(self):
        tk.Button(self.root, text="Выберите файл", command=select_file).pack()


if __name__ == '__main__':
    app = Window()
    app.run()
