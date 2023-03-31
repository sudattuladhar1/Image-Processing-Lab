import cv2 as cv
from otsu_Thresholding import Ui_Dialog

from PyQt5.QtWidgets import (
    QDialog
)

class OtsuThresholdDialog(Ui_Dialog, QDialog):
    OPTIONS = {
        'BINARY':cv.THRESH_BINARY,
        'BINARY_INV':cv.THRESH_BINARY_INV,
        'BINARY + OTSU':cv.THRESH_BINARY + cv.THRESH_OTSU,
        'BINARY_INV + OTSU':cv.THRESH_BINARY_INV + cv.THRESH_OTSU
    }

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.options.addItems(self.OPTIONS.keys())
        # Default settings
        self.options.setCurrentText('BINARY + OTSU')

    def getLower(self):
        return self.slider_lower.value()

    def getHigher(self):
        return self.slider_upper.value()

    def getOption(self):
        return self.options.currentText()
    
    def enableThresholds(self, enable = True):
        self.slider_lower.setEnabled(enable)
        self.slider_upper.setEnabled(enable)

    def setThresholdsLabels(self, lower, upper):
        self.label_lower.setText(str(lower))
        self.label_upper.setText(str(upper))

