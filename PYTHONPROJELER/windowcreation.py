from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon 
from PyQt5.QtCore import Qt 
import sys 

class MyWindow(QWidget): 
    def init (self): 
        super().init()
        self.initUI()


if __name__== "__main__":
    app = QApplication(sys.argv)
    win = MyWindow() 
    win.show() 
    sys.exit(app.exec_())
