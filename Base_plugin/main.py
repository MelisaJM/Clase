import os
import sys

from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt5.QtCore import *
from Pyt5.QtWidgets import *

from .interfaz import Ui_MainWindow

#crear clase
class main_interfaz(QMainWindow):
    def __init_(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)