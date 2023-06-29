from moviepy.editor import *
from pathlib import Path
import os


def convert(file_path):
    video = VideoFileClip(f'{file_path}')
    audio = video.audio
    save_directory = './'
    os.makedirs(save_directory, exist_ok=True)
    save_path = f'{save_directory}/{Path(file_path).stem}.mp3'
    audio.write_audiofile(save_path)
