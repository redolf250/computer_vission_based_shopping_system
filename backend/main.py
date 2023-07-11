import os
import sys
from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from dashboard.ui_dashboard import Ui_MainWindow
from launcher.ui_launcher import Ui_Launcher


GLOBAL_STATE = 0
counter = 0

class Main(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
    
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())  
        
        self.ui_main.btn_close.clicked.connect(self.close)
        self.ui_main.btn_minimize.clicked.connect(self.showMinimized)

        self.ui_main.btn_home.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.home))
        self.ui_main.btn_cart.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.cart))
        self.ui_main.btn_update.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.update))
        self.ui_main.btn_option.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.page)) 

    def resource_path(self,relative_path):
        path= os.path.abspath(os.path.join(os.path.dirname(__file__),relative_path)) 
        return path   
    
    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()  

class Launcher(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_splash = Ui_Launcher()
        self.ui_splash.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 70))
        self.ui_splash.main.setGraphicsEffect(self.shadow)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.show()

    def progress(self):
        global counter
        self.ui_splash.progressBar.setValue(counter)
        if counter > 50:
            self.timer.stop()
            self.close()  
            self.main = Main()
            self.main.show()        
        counter +=1


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Launcher() 
    sys.exit(application.exec_()) 
