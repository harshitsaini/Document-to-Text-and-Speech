#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
    name = 'doc2speech',
    version ='0.0.1',
    packages =find_packages(),
    description = 'Python package for online kannada optical character recognition',
    # url = '',
    author = 'Harshit Saini',
    # license = 'MIT',
    author_email = 'harshitsaini15@gmail.com',
    install_requires = ['gTTS==2.0.3', 'numpy==1.16.1',
                        'opencv-python==4.0.0.21',
                        'Pillow==5.4.1', 'pytesseract==0.2.6'],
    keywords = 'gtts OpenCV'
    )
