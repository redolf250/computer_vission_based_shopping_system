# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcherbUJojQ.ui'
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


class Ui_Launcher(object):
    def setupUi(self, Launcher):
        if Launcher.objectName():
            Launcher.setObjectName(u"Launcher")
        Launcher.resize(406, 283)
        self.centralwidget = QWidget(Launcher)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.main = QFrame(self.centralwidget)
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"QFrame{	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(66, 66, 66);\n"
"}")
        self.main.setFrameShape(QFrame.NoFrame)
        self.main.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 60, 281, 71))
        font = QFont()
        font.setFamily(u"Modern No. 20")
        font.setPointSize(40)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 160, 251, 21))
        font1 = QFont()
        font1.setFamily(u"Modern No. 20")
        font1.setPointSize(14)
        font1.setItalic(False)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.main)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 260, 1001, 16))
        self.progressBar.setStyleSheet(u"QProgressBar{	\n"
"	background-color: rgb(98, 114, 164);\n"
"	border-style:none;\n"
"	text-align:center;\n"
"	color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"")
        self.progressBar.setValue(10)
        self.progressBar.setTextVisible(False)
        self.image = QLabel(self.main)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(870, 450, 111, 101))

        self.verticalLayout.addWidget(self.main)

        Launcher.setCentralWidget(self.centralwidget)

        self.retranslateUi(Launcher)

        QMetaObject.connectSlotsByName(Launcher)
    # setupUi

    def retranslateUi(self, Launcher):
        Launcher.setWindowTitle(QCoreApplication.translate("Launcher", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Launcher", u"<html><head/><body><p>iShop</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Launcher", u"<html><head/><body><p>Shopping made easy!</p></body></html>", None))
        self.image.setText("")
    # retranslateUi

