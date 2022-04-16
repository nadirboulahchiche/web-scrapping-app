# -*- coding: utf-8 -*-

################################################################################
## 
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
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(190, 0, 441, 291))
        self.groupBox.setLayoutDirection(Qt.RightToLeft)
        self.groupBox.setStyleSheet(u"background-color: rgb(198, 198, 198);")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 421, 261))
        self.frame.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.data_links = QLabel(self.frame)
        self.data_links.setObjectName(u"data_links")
        self.data_links.setGeometry(QRect(0, 0, 421, 261))
        self.data_links.setLayoutDirection(Qt.RightToLeft)
        self.data_links.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                             u"color: rgb(0, 0, 255);")
        self.data_links.setFrameShadow(QFrame.Plain)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 0, 181, 291))
        self.groupBox_2.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(198, 198, 198);")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.create_dir = QPushButton(self.groupBox_2)
        self.create_dir.setObjectName(u"create_dir")
        font = QFont()
        font.setPointSize(16)
        self.create_dir.setFont(font)
        self.create_dir.setFocusPolicy(Qt.ClickFocus)
        self.create_dir.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.create_dir)

        self.add = QPushButton(self.groupBox_2)
        self.add.setObjectName(u"add")
        self.add.setFont(font)
        self.add.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.add)

        self.download = QPushButton(self.groupBox_2)
        self.download.setObjectName(u"download")
        self.download.setFont(font)
        self.download.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.download)

        self.remove = QPushButton(self.groupBox_2)
        self.remove.setObjectName(u"remove")
        self.remove.setFont(font)
        self.remove.setStyleSheet(u"background-color: rgb(202, 202, 202);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.remove)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(190, 290, 441, 161))
        self.groupBox_3.setStyleSheet(u"background-color: rgb(198, 198, 198);")
        self.downloaded = QLabel(self.groupBox_3)
        self.downloaded.setObjectName(u"downloaded")
        self.downloaded.setGeometry(QRect(10, 20, 421, 131))
        self.downloaded.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.quit = QPushButton(self.centralwidget)
        self.quit.setObjectName(u"quit")
        self.quit.setGeometry(QRect(10, 370, 151, 61))
        self.quit.setFont(font)
        self.quit.setStyleSheet(u"background-color: rgb(198, 198, 198);\n"
"color: rgb(255, 0, 0);")
        self.path_dir = QLabel(self.centralwidget)
        self.path_dir.setObjectName(u"path")
        self.path_dir.setGeometry(QRect(10, 300, 161, 41))
        font1 = QFont()
        font1.setPointSize(6)
        self.path_dir.setFont(font1)
        self.path_dir.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"all links", None))
        self.data_links.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"options", None))
        self.create_dir.setText(QCoreApplication.translate("MainWindow", u"load directory", None))
        self.add.setText(QCoreApplication.translate("MainWindow", u"add link", None))
        self.download.setText(QCoreApplication.translate("MainWindow", u"download images", None))
        self.remove.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"all downloaded data", None))
        self.downloaded.setText("")
        self.quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.path_dir.setText(QCoreApplication.translate("MainWindow", u"None", None))
    # retranslateUi

