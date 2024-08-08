from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush, QPixmap, QBitmap, QPalette
from PyQt5.QtCore import Qt, QPoint, QRect, QSize
from scipy import signal
import numpy as np
from xyt import xyeta
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radiobaton = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobaton.setGeometry(QtCore.QRect(30, 40, 20, 20))
        self.radiobaton.setObjectName("radiobaton")
        self.radiobaton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobaton2.setGeometry(QtCore.QRect(50, 40, 20, 20))
        self.radiobaton2.setObjectName("radiobaton2")
        self.radiobaton3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radiobaton3.setGeometry(QtCore.QRect(70, 40, 20, 20))
        self.radiobaton3.setObjectName("radiobaton3")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(50, 10, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(110, 10, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(170, 10, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        # self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget = xyeta(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(59, 89, 800, 700))
        self.widget.setAutoFillBackground(True)
        self.widget.setObjectName("widget")
        # self.image = QImage(self.widget.size(), QImage.Format_RGB32)
        # self.image.fill(Qt.black)
        # self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        # self.horizontalSlider.setGeometry(QtCore.QRect(350, 20, 160, 22))
        # self.horizontalSlider.setProperty("value", 50)
        # self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        # self.horizontalSlider.setObjectName("horizontalSlider")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        # self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGeometry(QtCore.QRect(410, 50, 55, 16))
        # self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        # self.label.setText(_translate("MainWindow", "Дуть"))
