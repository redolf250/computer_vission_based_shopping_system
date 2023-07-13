import os
import cv2
import sys
import uuid
import numpy as np
from datetime import datetime

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
        self.saveTimer = QTimer()
        self.ui_main.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
    
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft()) 

        self.ui_main.btn_connect.clicked.connect(self.start_webcam)
        self.ui_main.btn_disconnect.clicked.connect(self.stop_webcam) 
        
        self.ui_main.btn_close.clicked.connect(self.close)
        self.ui_main.btn_minimize.clicked.connect(self.showMinimized)

        self.ui_main.btn_home.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.home))
        self.ui_main.btn_cart.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.cart))
        self.ui_main.btn_update.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.update))
        self.ui_main.btn_option.clicked.connect(lambda: self.ui_main.stackedWidget.setCurrentWidget(self.ui_main.page))
        self.set_mall_details(self.read_mall_details(self.resource_path('mall_details.txt')))

        self.ui_main.btn_connect_2.clicked.connect(self.cart_items)

    def read_mall_details(self, filepath):
        number = uuid.uuid1()
        number = str(number).split('-')[4]
        with open(filepath, 'r') as content:
            details=content.read()
        return str(details).replace('dateStamp',datetime.now().date().strftime('%d-%m-%Y')).replace('receiptNumber',number)
       
    def set_mall_details(self, data):
        self.ui_main.textEdit.append(data)

    def cart_items(self):
        products = self.parse_data()
        total = 0
        for key, value in products.items():
            self.ui_main.textEdit.append(f'{key} {value}')
            amount = str(value).split('\t')[4].strip()
            self.ui_main.textEdit.append("======================================")
            total+=int(amount)
        print(total)
        pass

    def parse_data(self):
        items = {}
        items['347685068'] = "       \t100      \t200   \t\t2000"
        return items

    def start_webcam(self):
        self.show_info("Starting webcam in\nprogress.")
        self.system_capture = cv2.VideoCapture(0)
        self.show_info("Starting webcam in\nprogress.")
        self.system_capture.set(cv2.CAP_PROP_FRAME_HEIGHT,280)
        self.system_capture.set(cv2.CAP_PROP_FRAME_WIDTH,450)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(3)
        self.show_info("Starting webcam in\nprogress.")
            
    def update_frame(self):

        thickness = 2
        rect_thickness = 1
        color = (255,255,0)
        
        ret,self.frame = self.system_capture.read()
        self.frame = cv2.flip(self.frame,1)

        self.display_feed(self.frame,1)         
        
    def display_feed(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        procesedImage = procesedImage.rgbSwapped()
        if window == 1:
            self.ui_main.cameraFeed.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui_main.cameraFeed.setScaledContents(True)
        
    def stop_webcam(self):
        if self.timer.isActive():
            self.show_info("Disconnecting from\nwebcam.")
            self.ui_main.cameraFeed.setPixmap(u":/icons/asset/camera-off.svg")
            self.ui_main.cameraFeed.setScaledContents(False)
            self.timer.stop() 
        else:
            self.show_info("Oops! no camera\nin use.") 

    def show_info(self, content:str):
        self.ui_main.label_notification.setText(content)

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
