import os
import sys
from PyQt5 import QtGui

# =====================
# RESOURCE PATH (CROSS PLATFORM)
# =====================
def resource_path(relative_path):
    """ Get absolute path to resource (works for dev + bundled app) """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # for bundled apps (py2app / pyinstaller)
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# =====================
# GIF LOADER
# =====================

# Path to your GIF folder
ASSET_DIR = resource_path("zugeschnitten_gifs")

def load_gif(name, frame_count):
    path = os.path.join(ASSET_DIR, name)
    
    if not os.path.exists(path):
        print(f"ERROR: File not found -> {path}")
    
    frames = []
    movie = QtGui.QMovie(path)
    
    for i in range(frame_count):
        movie.jumpToFrame(i)
        frames.append(movie.currentPixmap())
    
    return frames