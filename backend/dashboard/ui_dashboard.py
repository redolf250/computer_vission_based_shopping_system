# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardqsmoCO.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(780, 462)
        MainWindow.setMinimumSize(QSize(0, 400))
        MainWindow.setMaximumSize(QSize(780, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.mainWindow = QWidget(MainWindow)
        self.mainWindow.setObjectName(u"mainWindow")
        self.mainWindow.setMinimumSize(QSize(780, 460))
        self.mainWindow.setMaximumSize(QSize(780, 460))
        self.mainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.verticalLayout = QVBoxLayout(self.mainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.mainWindow)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(80, 80, 80);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(480, 0))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"background-color: rgb(80, 80, 80);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 9, -1, 0)
        self.btn_home = QPushButton(self.frame_3)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(10)
        self.btn_home.setFont(font)
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-bottom: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
" QPushButton:focus{\n"
"    color: rgb(255, 255, 255);\n"
"    border-bottom: 2px solid rgb(255,255,255);	\n"
"  }")
        icon = QIcon()
        icon.addFile(u"../../../shopping/resource/asset/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(30, 30))
        self.btn_home.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_home)

        self.btn_cart = QPushButton(self.frame_3)
        self.btn_cart.setObjectName(u"btn_cart")
        self.btn_cart.setMaximumSize(QSize(100, 40))
        self.btn_cart.setFont(font)
        self.btn_cart.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-bottom: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
" QPushButton:focus{\n"
"    color: rgb(255, 255, 255);\n"
"    border-bottom: 2px solid rgb(255,255,255);	\n"
"  }")
        icon1 = QIcon()
        icon1.addFile(u"../resource/asset/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cart.setIcon(icon1)
        self.btn_cart.setIconSize(QSize(30, 30))
        self.btn_cart.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_cart)

        self.btn_update = QPushButton(self.frame_3)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMaximumSize(QSize(100, 40))
        self.btn_update.setFont(font)
        self.btn_update.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-bottom: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
" QPushButton:focus{\n"
"    color: rgb(255, 255, 255);\n"
"    border-bottom: 2px solid rgb(255,255,255);	\n"
"  }")
        icon2 = QIcon()
        icon2.addFile(u"../resource/asset/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon2)
        self.btn_update.setIconSize(QSize(30, 30))
        self.btn_update.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_update)

        self.btn_option = QPushButton(self.frame_3)
        self.btn_option.setObjectName(u"btn_option")
        self.btn_option.setMaximumSize(QSize(100, 40))
        self.btn_option.setFont(font)
        self.btn_option.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(80, 80, 80);\n"
"	border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-bottom: 3px solid rgb(255,255,255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-bottom: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
" QPushButton:focus{\n"
"    color: rgb(255, 255, 255);\n"
"    border-bottom: 2px solid rgb(255,255,255);	\n"
"  }")
        icon3 = QIcon()
        icon3.addFile(u"../resource/asset/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_option.setIcon(icon3)
        self.btn_option.setIconSize(QSize(30, 30))
        self.btn_option.setFlat(True)

        self.horizontalLayout_5.addWidget(self.btn_option)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color: rgb(80, 80, 80);\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.cartTotalItemsTopBAr = QLabel(self.frame_4)
        self.cartTotalItemsTopBAr.setObjectName(u"cartTotalItemsTopBAr")
        self.cartTotalItemsTopBAr.setGeometry(QRect(30, 10, 91, 35))
        self.cartTotalItemsTopBAr.setMinimumSize(QSize(35, 35))
        self.cartTotalItemsTopBAr.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setWeight(50)
        self.cartTotalItemsTopBAr.setFont(font1)
        self.cartTotalItemsTopBAr.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 20px;\n"
"}")
        self.cartTotalItemsTopBAr.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(150, 16777215))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.btn_maximize = QPushButton(self.frame_5)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(65, 7, 30, 30))
        self.btn_maximize.setMinimumSize(QSize(30, 30))
        self.btn_maximize.setMaximumSize(QSize(30, 30))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"background-color: rgb(120, 117, 113);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../resource/asset/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon4)
        self.btn_maximize.setIconSize(QSize(30, 30))
        self.btn_close = QPushButton(self.frame_5)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(110, 7, 30, 30))
        self.btn_close.setMinimumSize(QSize(30, 30))
        self.btn_close.setMaximumSize(QSize(30, 30))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(255, 0, 0);\n"
"	\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../resource/asset/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon5)
        self.btn_close.setIconSize(QSize(30, 30))
        self.btn_minimize = QPushButton(self.frame_5)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(20, 10, 30, 30))
        self.btn_minimize.setMinimumSize(QSize(30, 30))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"background-color: rgb(80, 80, 80)\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgb(120, 117, 113);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../resource/asset/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon6)
        self.btn_minimize.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(self.mainWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(780, 400))
        self.stackedWidget.setMaximumSize(QSize(780, 400))
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(0, 410))
        self.horizontalLayout_2 = QHBoxLayout(self.home)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.home)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(0, 0, 241, 191))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.image.setFont(font2)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setPixmap(QPixmap(u"../resource/asset/image.svg"))
        self.image.setAlignment(Qt.AlignCenter)
        self.label_notification = QLabel(self.frame)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(0, 320, 241, 61))
        font3 = QFont()
        font3.setFamily(u"MS Shell Dlg 2")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_notification.setFont(font3)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 5px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.label_notification.setWordWrap(True)
        self.itemId = QLabel(self.frame)
        self.itemId.setObjectName(u"itemId")
        self.itemId.setGeometry(QRect(0, 200, 131, 45))
        self.itemId.setMinimumSize(QSize(45, 45))
        self.itemId.setFont(font3)
        self.itemId.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.itemId.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.itemPrice = QLabel(self.frame)
        self.itemPrice.setObjectName(u"itemPrice")
        self.itemPrice.setGeometry(QRect(150, 200, 91, 45))
        self.itemPrice.setMinimumSize(QSize(45, 45))
        self.itemPrice.setFont(font3)
        self.itemPrice.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.itemPrice.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.itemName = QLabel(self.frame)
        self.itemName.setObjectName(u"itemName")
        self.itemName.setGeometry(QRect(0, 260, 241, 45))
        self.itemName.setMinimumSize(QSize(45, 45))
        self.itemName.setFont(font3)
        self.itemName.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"\n"
"}")
        self.itemName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_6 = QFrame(self.home)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 330))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.cameraFeed = QLabel(self.frame_7)
        self.cameraFeed.setObjectName(u"cameraFeed")
        self.cameraFeed.setMaximumSize(QSize(500, 16777215))
        font4 = QFont()
        font4.setPointSize(11)
        self.cameraFeed.setFont(font4)
        self.cameraFeed.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 10px;\n"
"}")
        self.cameraFeed.setPixmap(QPixmap(u"../resource/asset/camera.svg"))
        self.cameraFeed.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.cameraFeed)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 60))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.btn_disconnect = QPushButton(self.frame_8)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setGeometry(QRect(270, 10, 231, 45))
        self.btn_disconnect.setMinimumSize(QSize(0, 45))
        self.btn_disconnect.setMaximumSize(QSize(16777215, 45))
        self.btn_disconnect.setFont(font)
        self.btn_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../../../shopping/resource/asset/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_disconnect.setIcon(icon7)
        self.btn_disconnect.setIconSize(QSize(30, 30))
        self.btn_disconnect.setFlat(True)
        self.btn_connect = QPushButton(self.frame_8)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setGeometry(QRect(0, 10, 241, 45))
        self.btn_connect.setMinimumSize(QSize(0, 45))
        self.btn_connect.setMaximumSize(QSize(16777215, 45))
        self.btn_connect.setFont(font)
        self.btn_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"../../../shopping/resource/asset/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_connect.setIcon(icon8)
        self.btn_connect.setIconSize(QSize(30, 30))
        self.btn_connect.setFlat(True)

        self.verticalLayout_2.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.home)
        self.update = QWidget()
        self.update.setObjectName(u"update")
        self.label = QLabel(self.update)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 170, 241, 61))
        font5 = QFont()
        font5.setPointSize(16)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.update)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 160, 241, 61))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page)
        self.cart = QWidget()
        self.cart.setObjectName(u"cart")
        self.cart.setMinimumSize(QSize(0, 0))
        self.cart.setMaximumSize(QSize(16777215, 460))
        self.horizontalLayout_3 = QHBoxLayout(self.cart)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_9 = QFrame(self.cart)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(230, 0))
        self.frame_9.setMaximumSize(QSize(200, 16777215))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.cartProducts = QComboBox(self.frame_9)
        self.cartProducts.setObjectName(u"cartProducts")
        self.cartProducts.setGeometry(QRect(0, 70, 221, 45))
        self.cartProducts.setMinimumSize(QSize(0, 45))
        self.cartProducts.setMaximumSize(QSize(16777215, 45))
        self.cartProducts.setFont(font)
        self.cartProducts.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.cartProducts.setFrame(False)
        self.quantity = QLineEdit(self.frame_9)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setGeometry(QRect(110, 130, 111, 45))
        self.quantity.setMinimumSize(QSize(0, 45))
        self.quantity.setMaximumSize(QSize(16777215, 45))
        self.quantity.setFont(font)
        self.quantity.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(66, 66, 66);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.quantity.setClearButtonEnabled(True)
        self.btn_calculateTotal = QPushButton(self.frame_9)
        self.btn_calculateTotal.setObjectName(u"btn_calculateTotal")
        self.btn_calculateTotal.setGeometry(QRect(0, 200, 221, 45))
        self.btn_calculateTotal.setMinimumSize(QSize(0, 45))
        self.btn_calculateTotal.setMaximumSize(QSize(16777215, 45))
        self.btn_calculateTotal.setFont(font)
        self.btn_calculateTotal.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_calculateTotal.setIconSize(QSize(30, 30))
        self.btn_calculateTotal.setFlat(True)
        self.cartTotalItems = QLabel(self.frame_9)
        self.cartTotalItems.setObjectName(u"cartTotalItems")
        self.cartTotalItems.setGeometry(QRect(0, 10, 91, 45))
        self.cartTotalItems.setMinimumSize(QSize(45, 45))
        self.cartTotalItems.setFont(font3)
        self.cartTotalItems.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 5px;\n"
"}")
        self.cartTotalItems.setAlignment(Qt.AlignCenter)
        self.cart_notification = QLabel(self.frame_9)
        self.cart_notification.setObjectName(u"cart_notification")
        self.cart_notification.setGeometry(QRect(0, 320, 221, 71))
        self.cart_notification.setFont(font3)
        self.cart_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 85, 85);\n"
"	border-radius: 5px;\n"
"}")
        self.cart_notification.setAlignment(Qt.AlignCenter)
        self.cart_notification.setWordWrap(True)
        self.cartTotalAmount = QLabel(self.frame_9)
        self.cartTotalAmount.setObjectName(u"cartTotalAmount")
        self.cartTotalAmount.setGeometry(QRect(110, 10, 111, 45))
        self.cartTotalAmount.setMinimumSize(QSize(45, 45))
        self.cartTotalAmount.setFont(font3)
        self.cartTotalAmount.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 5px;\n"
"}")
        self.cartTotalAmount.setAlignment(Qt.AlignCenter)
        self.productPrice = QLabel(self.frame_9)
        self.productPrice.setObjectName(u"productPrice")
        self.productPrice.setGeometry(QRect(0, 130, 91, 45))
        self.productPrice.setMinimumSize(QSize(45, 45))
        self.productPrice.setFont(font3)
        self.productPrice.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border-radius: 5px;\n"
"}")
        self.productPrice.setAlignment(Qt.AlignCenter)
        self.btn_printReceipt = QPushButton(self.frame_9)
        self.btn_printReceipt.setObjectName(u"btn_printReceipt")
        self.btn_printReceipt.setGeometry(QRect(0, 260, 221, 45))
        self.btn_printReceipt.setMinimumSize(QSize(0, 45))
        self.btn_printReceipt.setMaximumSize(QSize(16777215, 45))
        self.btn_printReceipt.setFont(font)
        self.btn_printReceipt.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"	border:none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"../../../shopping/resource/asset/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_printReceipt.setIcon(icon9)
        self.btn_printReceipt.setIconSize(QSize(30, 30))
        self.btn_printReceipt.setFlat(True)

        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.cart)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 400))
        self.frame_10.setMaximumSize(QSize(16777215, 450))
        self.frame_10.setFont(font)
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 4, 0, 4)
        self.textEdit = QTextEdit(self.frame_10)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding:15px;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.textEdit)


        self.horizontalLayout_3.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.cart)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.mainWindow)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cart.setText(QCoreApplication.translate("MainWindow", u"Cart", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.btn_option.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.cartTotalItemsTopBAr.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_maximize.setText("")
        self.btn_close.setText("")
        self.btn_minimize.setText("")
        self.image.setText("")
        self.label_notification.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.itemId.setText(QCoreApplication.translate("MainWindow", u"Product Id", None))
        self.itemPrice.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.itemName.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.cameraFeed.setText("")
        self.btn_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.quantity.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Quantity", None))
        self.btn_calculateTotal.setText(QCoreApplication.translate("MainWindow", u"Calculate Total", None))
        self.cartTotalItems.setText(QCoreApplication.translate("MainWindow", u"Items", None))
        self.cart_notification.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.cartTotalAmount.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.productPrice.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.btn_printReceipt.setText(QCoreApplication.translate("MainWindow", u"Print Receipt", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

