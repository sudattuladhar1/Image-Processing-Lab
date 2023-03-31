import sys
import cv2 as cv
import matplotlib.pyplot as plt
#import imutils

from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread, QTimer
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtWidgets import (
    QApplication, QMainWindow,qApp,
    QFileDialog, QDialog,
    QPushButton, QLabel, QSlider,
    QComboBox, QSpinBox, 
)