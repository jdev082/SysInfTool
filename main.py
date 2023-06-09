#!/usr/bin/env python3
"""
SysInfTool v1.0
MIT License, 2023
jdev082 (https://github.com/jdev082)
"""

# Library Imports
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QScrollArea
from functions import *

# Data Imports
from appmeta import *
from content import *

# Arguments

if len(sys.argv) > 1:
    if sys.argv[1] == '-o' or sys.argv[1] == '--out':
        content = content.replace("<h1>", "\033[1m")
        content = content.replace("</h1>", "\033[0m")
        content = content.replace("<h2>", "\033[1m")
        content = content.replace("</h2>", "\033[0m")
        content = content.replace("<p>", " ")
        content = content.replace("</p>", " ")
        content = content.replace("<pre>", " ")
        content = content.replace("</pre>", " ")
        print(content)
        exit()
    if sys.argv[1] == 'h' or sys.argv[1] == '--help':
        print('./main.py (-o/--out output in terminal)')

# Application
app = QApplication([])

window = QWidget()
window.setWindowTitle(nam)
window.setFixedSize(500, 600)

scroll = QScrollArea(parent=window)
info = QLabel(content, parent=scroll)
scroll.setWidget(info)
scroll.setFixedSize(500, 600)
window.show()

sys.exit(app.exec())