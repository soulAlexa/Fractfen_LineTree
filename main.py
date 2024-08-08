import random

import scipy.special
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog, QSpinBox
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush, QPixmap, QBitmap, QPalette, QColor
from PyQt5.QtCore import Qt, QPoint, QRect, QSize
from scipy import signal
from random import randint
import numpy as np
import math
import sys
from qt import Ui_MainWindow
import sys


class mywindow(QtWidgets.QMainWindow):
    _lv = 0
    _w = 0
    _h = 0
    _spin1 = 0
    _spin2 = 0
    _spin3 = 0
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):

        image = QImage()
        self.ui.widget.setcufrac(image)
        self.fractfen()
        self.ui.pushButton.clicked.connect(self.run)



    def run(self):
        if self.ui.radiobaton.isChecked():
            self._spin1 = self.ui.spinBox
            self._spin1.valueChanged.connect(self.carpetFrac)
        if self.ui.radiobaton2.isChecked():
            self._spin1 = self.ui.spinBox
            self._spin1.valueChanged.connect(self.drawLineTree)
            self._spin2 = self.ui.spinBox_2
            self._spin2.valueChanged.connect(self.drawLineTree)
            self._spin3 = self.ui.spinBox_3
            self._spin3.valueChanged.connect(self.drawLineTree)
        if self.ui.radiobaton3.isChecked():
            self._spin1 = self.ui.spinBox
            self._spin1.valueChanged.connect(self.factor)
    def fractfen(self):
        self._w = self.ui.widget.width()
        self._h = self.ui.widget.height()
        self._lv = self.ui.spinBox.value()
        size = self._h
        map = QImage(self._w, self._h, QImage.Format_RGB32)
        map.fill(Qt.black)
        paintr = QPainter(map)
        paintr.setPen(Qt.white)
        x, y = 0, 0
        Koeficients = [[0, 0, 0, .16, 0, 0],
                       [.85, .04, -.04, .85, 0, 1.6],
                       [.2, -.26, .23, .22, 0, 1.6],
                       [-.15, .28, .26, .24, 0, .44]]
        for i in range(50000):
            P = random.randint(0, 100)

            if P == 0:
                XY = self.somefunc(x, y, *Koeficients[0])
            elif P < 85:
                XY = self.somefunc(x, y, *Koeficients[1])
            elif P < 93:
                XY = self.somefunc(x, y, *Koeficients[2])
            else:
                XY = self.somefunc(x, y, *Koeficients[3])

            x = XY[0].item()
            y = XY[1].item()

            m = QPoint(int(x * 60 + 300), int(y * 60))
            n = QPoint(int(x * 60 + 300), int(y * 60))
            paintr.drawLine(m, n)

        self.ui.widget.setcufrac(map)
        self.ui.widget.update()

    def somefunc(self, x, y, a, b, c, d, e, f):
        return np.matrix([[a, b], [c, d]]) * np.matrix([[x], [y]]) + np.matrix([[e], [f]])

    def factor(self):
        number = self.ui.spinBox.value()
        self._w = self.ui.widget.width()
        self._h = self.ui.widget.height()
        self._lv = self.ui.spinBox.value()
        size = self._h
        map = QImage(self._w, self._h, QImage.Format_RGB32)
        map.fill(Qt.white)
        paintr = QPainter(map)
        k = self.factorStep(number, 0)
        paintr.setPen(Qt.black)
        paintr.drawText(300, 200, "Факториал равен = " + str(k))
        self.ui.widget.setcufrac(map)
        self.ui.widget.update()



    def factorStep(self, number, ll):
        if number <= 1:
            ll = number
            return 1
        else:
            return number * self.factorStep(number - 1, ll)



    def drawLineTree(self):
        self._w = self.ui.widget.width()
        self._h = self.ui.widget.height()
        self._lv = self.ui.spinBox.value()
        size = self._h
        map = QImage(self._w, self._h, QImage.Format_RGB32)
        map.fill(Qt.white)
        paintr = QPainter(map)
        self.drawLineTreeStep(paintr, QPoint(int(self._w/2), int(self._h)), self._h/2.5, float(self.ui.spinBox_2.value()) * np.pi/180,
                              float(self.ui.spinBox_3.value()) * np.pi/180, QColor(0x00FF00), QColor(0xFF0000))
        self.ui.widget.setcufrac(map)
        self.ui.widget.update()

    def drawLineTreeStep(self, paintr, p, a, an1, an2, c1, c2, angle = float(np.pi / 2), level = 0):
        if level > self._lv:
            return
        paintr.setPen(QPen(self.getInter(c1, c2, level, self._lv), 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

        a *= float(np.sqrt(2) / 2)
        t = QPoint(int(p.x() + a * np.cos(angle)), int(p.y() - a * np.sin(angle)))
        paintr.drawLine(p, t)

        self.drawLineTreeStep(paintr, t, a, an1, an2, c1, c2, angle + an1, level + 1)
        self.drawLineTreeStep(paintr, t, a, an1, an2, c1, c2, angle - an2, level + 1)

    def carpetFrac(self):
        self._w = self.ui.widget.width()
        self._h = self.ui.widget.height()
        self._lv = self.ui.spinBox.value()
        size = self._h
        map = QImage(self._w, self._h, QImage.Format_RGB32)
        map.fill(Qt.white)
        paintr = QPainter(map)
        r = QRect(int((self._w - size) / 2), int((self._h - size) / 2), size, size)
        self.DrawCarpetfracstep(paintr, r, QColor(0x00FF00), QColor(0xFF0000))
        self.ui.widget.setcufrac(map)
        self.ui.widget.update()

    def DrawCarpetfracstep(self, paintr, r, c1, c2, level=0):
        if level > self._lv:
            return
        # paintr.setPen(QPen(self.getInter(c1, c2, level, self._lv), 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        nSize = QSize(int(r.width() / 3), int(r.height() / 3))
        hole = QRect(QPoint(r.x() + nSize.width(), r.y() + nSize.height()), nSize)
        paintr.fillRect(r, self.getInter(c1, c2, level, self._lv))
        paintr.fillRect(hole, Qt.white)
        rs = []
        for i in range(3):
            for ii in range(3):
                if i != 1 and ii != 1:
                    rs.append(QRect(QPoint(r.x() + nSize.width() * i, r.y() + nSize.height() * ii), nSize))

        for n in rs:
            self.DrawCarpetfracstep(paintr, n, c1, c2, level + 1)

    def getInter(self, c1, c2, cur, n):
        if n == 0:
            return c1
        t1 = float((n - cur) / n)
        t2 = float(cur / n)
        r = c1.red() * t1 + c2.red() * t2
        g = c1.green() * t1 + c2.green() * t2
        b = c1.blue() * t1 + c2.blue() * t2
        a = c1.alpha() * t1 + c2.alpha() * t2
        return QColor(math.floor(r), math.floor(g), math.floor(b), math.floor(a))



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())

