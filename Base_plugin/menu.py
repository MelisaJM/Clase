import os
import sys

from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt5.QtCore import *
from Pyt5.QtWidgets import *

from .main import main_interfaz

class menuInit:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.EMenu = QMenu(self.iface.mainWindow())
        self.EMenu.setTitle("Ejemplo1")
        self.EMenuBar = self.iface.mainWindow().menuBar()
        self.EMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(),self.EMenu)
        self.EMenuBar = self.iface.addToolBar("Ejemplo")

        self.action = QAction(QIcon(":/Base_plugin/icon.png"),"Ejemplo",self.iface.mainWindow())
        self.EMenu.addAction(self.action)
        self.action.triggered.connect(self.dialogo)
        
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Ejemplo",self.action)

    def dialogo(self):
        self.diag = main_interfaz() #Se trae la clase del archivo main
        self.diag.show()
    