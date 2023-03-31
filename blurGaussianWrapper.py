import cv2 as cv
from blurGaussian import Ui_Dialog
from PyQt5.QtWidgets import QDialog

class GaussianBlurDialog(Ui_Dialog, QDialog):
    BORDER_TYPE = {
        'CONSTANT':cv.BORDER_CONSTANT,
        'RPELICATE': cv.BORDER_REPLICATE,
        'REFLECT': cv.BORDER_REFLECT,
        'WRAP': cv.BORDER_WRAP,
        'REFLECT 101': cv.BORDER_REFLECT_101,
        'TRANSPARENT':  cv.BORDER_TRANSPARENT, 
        'DEFAULT': cv.BORDER_DEFAULT,
        'ISOLATED': cv.BORDER_ISOLATED
    }
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Extra setup
        self.blurGaussianBorderTypecomboBox.addItems(self.BORDER_TYPE.keys())

    def getKernelSize(self):
        return self.blurGaussianKernelSizespinBox.value()
    
    def getBorderType(self):
        return self.BORDER_TYPE[self.blurGaussianBorderTypecomboBox.currentText()]