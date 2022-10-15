from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from instr import *

class Win3(QWidget):
    def __init__(self):
        super().__init__()
        self.set_apppear()
        self.initUI()
        self.connects()
        self.show()

    def set_apppear(self):
        self.setWindowTitle( txt_title )
        self.resize( win_width, win_height )
        self.move( win_x, win_y )

    def initUI(self):
        pass
    
    def connects(self):
        pass
