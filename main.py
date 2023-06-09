"""
SysInfTool v1.0
MIT License, 2023
jdev082 (https://github.com/jdev082)
"""

# Library Imports
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from functions import *

# Data Imports
from appmeta import *
from content import *

# Application
app = QApplication([])

window = QWidget()
window.setWindowTitle(nam)
window.setFixedSize(340, 480)

info = QLabel(content, parent=window)
info.move(10, 15)

window.show()

sys.exit(app.exec())