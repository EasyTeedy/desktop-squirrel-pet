from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt5'],
    'includes': ['PyQt5.QtWidgets', 'PyQt5.QtGui', 'PyQt5.QtCore'],
    'resources': ['zugeschnitten_gifs'],  # 👈 THIS is important
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)