import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import shutil
from Convert import convert


def select_file():
    extensions = [("Video Files", ("*.avi", "*.mov", "*.mp4"))]
    file_path = filedialog.askopenfilename(filetypes=extensions)
    if file_path:
        save_path = filedialog.asksaveasfilename(defaultextension='.mp3')
        if save_path:
            convert_and_save(file_path, save_path)
        else:
            print("ERROR: No save path selected")
    else:
        print("ERROR: No file selected")


def convert_and_save(file_path, save_path):
    try:
        convert(file_path)
        shutil.move(f'./{Path(file_path).stem}.mp3', save_path)
        print("Файл успешно конвертирован и сохранен!")
    except Exception as e:
        print(f"Произошла ошибка при конвертации и сохранении файла: {str(e)}")
