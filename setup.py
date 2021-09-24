import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'name-%s%' % 'Load Compare',
    '--onefile',
    '--windowed',
    os.path.join('main.py'), """your script and path to the script"""
])