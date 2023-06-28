from tkinter import filedialog
from Convert import convert


def select_file():
    extensions = [("Video Files", ("*.avi", "*.mov", "*.mp4"))]
    file_path = filedialog.askopenfilename(filetypes=extensions)
    if file_path:
        convert(file_path)
    else:
        print("ERROR: No file selected")