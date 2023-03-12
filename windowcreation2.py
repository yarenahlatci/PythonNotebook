import sys 
from PyQt5 import QtWidgets #QtWidgets pencere, buton gibi özellikleri içinde barındırır.

def window():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget() 
    window.setWindowTitle("Let's create a window!") 
    window.show()
    sys.exit(app.exec_()) 

window() 
