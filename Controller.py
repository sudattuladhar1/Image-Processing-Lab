import cv2 as cv
import os.path
from MainApplication import MainApplication
from model import Model
from blurGaussianWrapper import GaussianBlurDialog
from otsuThresholdingWrapper import OtsuThresholdDialog
from PyQt5.QtWidgets import (
    qApp,
    QFileDialog,QDialog,QMainWindow
)
from PyQt5.QtGui import QPixmap, QImage

class Controller():
    def __init__(self):
        #super().__init__()
        self._model = Model()

        # Main Window
        self._windowMain = MainApplication()

        # Blur Gaussian Dialog Box
        self._windowBlurGaussian = GaussianBlurDialog()

        # Otsu Thresholding Dialog Box
        self._windowOtsuThresholding = OtsuThresholdDialog()

        # Defining Signals and Slots
        self._connectSignalsAndSlots()
        
        self._windowMain.show()
    
    def _connectSignalsAndSlots(self):
        # Menu actions
        self._windowMain.actionQuit.triggered.connect(self._exitApp)
        self._windowMain.actionQuit.triggered.connect(self._exitApp)
        self._windowMain.actionOpen.triggered.connect(self._openFile)
        self._windowMain.actionOpen_In_Gray.triggered.connect(self._openFileInGray)
        self._windowMain.actionSave.triggered.connect(self._saveFile)
        self._windowMain.actionInput_to_Output.triggered.connect(self._inputToOutput)
        self._windowMain.actionOutput_to_Input.triggered.connect(self._outputToInput)
        self._windowMain.actionTo_GrayScale.triggered.connect(self._convertToGrayScale)
        self._windowMain.actionInvert.triggered.connect(self._invert)
        #Signal Connects
        #Gaussian Blur
        self._windowMain.actionGaussian_Blur.triggered.connect(self._GaussianBlurUIHandler)
        self._windowBlurGaussian.blurGaussianBorderTypecomboBox.currentIndexChanged.connect(self._doGaussianBlur)
        self._windowBlurGaussian.blurGaussianKernelSizespinBox.valueChanged.connect(self._doGaussianBlur)
        # # Otsu Thresholding
        self._windowMain.actionOtsu.triggered.connect(self._dlgotsuThresholdUIHandler)
        self._windowOtsuThresholding.slider_lower.valueChanged.connect(self._doOtsuBlur)
        self._windowOtsuThresholding.slider_upper.valueChanged.connect(self._doOtsuBlur)
        self._windowOtsuThresholding.options.currentTextChanged.connect(self._doOtsuBlur)

    def _invert(self):
        self._model.invertImage()
        self.showImage()
        self._windowMain.msgLabel.setText(f'Image Inverted')

    def _inputToOutput(self):
        self._model.inputToOutput()
        self.showImage()
        self._windowMain.msgLabel.setText('Copy Input to Output')

    def _outputToInput(self):
        self._model.outputToInput()
        self._windowMain.msgLabel.setText('Copy Output to Input')

    def _dlgotsuThresholdUIHandler(self):
        if self._windowOtsuThresholding.exec():
            self._doOtsuBlur()

    def _doOtsuBlur(self):
        lower = self._windowOtsuThresholding.getLower()
        upper = self._windowOtsuThresholding.getHigher()
        option = self._windowOtsuThresholding.getOption()
        if option == 'BINARY + OTSU' or option == 'BINARY_INV + OTSU':
            lower = 0
            upper = 255
            self._windowOtsuThresholding.enableThresholds(False)
        else:
            self._windowOtsuThresholding.enableThresholds(True)
        self._windowOtsuThresholding.setThresholdsLabels(lower, upper)

        self._model.otsuThresholding(lower, upper, self._windowOtsuThresholding.OPTIONS[option])
        self.showImage()
        self._windowMain.msgLabel.setText(f'''
            Otsu Blur:
            lower : {lower},
            upper: {upper},
            method: {option}
            ''')

    def _doGaussianBlur(self):
        kernel_size = self._windowBlurGaussian.getKernelSize()
        borderType = self._windowBlurGaussian.getBorderType()
        self._model.gaussianBlur(kernel_size, borderType)
        self.showImage()
        self._windowMain.msgLabel.setText(f'''
            Doing Gaussian Blur:
            Kernel Size: {kernel_size},
            Border Type: {borderType}
        ''')

    def _GaussianBlurUIHandler(self):
        #self._windowBlurGaussian.show()
        #           OR
        if self._windowBlurGaussian.exec():
            self._doGaussianBlur()       

    def _convertToGrayScale(self):
        self._model.toGrayScale()
        self.showImage()
        self._windowMain.msgLabel.setText('Convert to Grayscale')

    def _exitApp(self):
        qApp.quit()

    def showImage(self):
        img = self._model.getOutputImage()
        if len(img.shape) == 3:
            height, width, channel = img.shape
            bytesPerLine = 3 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        else: 
            height, width = img.shape
            bytesPerLine = 1 * width
            qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_Indexed8)
        self._windowMain.imgLabel.setPixmap(QPixmap(qImg))

    def _openFile(self):
        # fdialog = QFileDialog(self)
        # fdialog.setDirectory(f'/Users/sudat/Documents/Notebooks/Project_PyOpenCV_PyQt5/assets')
        # fdialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        # fdialog.setNameFilter('Images (*.png *.jpg)')
        # fdialog.setviewMode(QFileDialog.ViewMode.List)
        # if fdialog.exec():
        filename = QFileDialog.getOpenFileName(
            self._windowMain,
            'Select a File',
            '/Users/sudat/Documents/Notebooks/Project_PyOpenCV_PyQt5/assets',
            'Images (*.png *.jpg);;All (*)'
        )
        if filename:
            self._windowMain.msgLabel.setText(f'File Opened: {filename[0]}')
            self._model.readImageFile(filename[0])
            self._model.inputToOutput()
            self.showImage()

    def _openFileInGray(self):
        filename = QFileDialog.getOpenFileName(
            self._windowMain,
            'Select a File',
            '/Users/sudat/Documents/Notebooks/Project_PyOpenCV_PyQt5/assets',
            'Images (*.png *.jpg);;All (*)'
        )
        if filename:
            self._windowMain.msgLabel.setText(f'File Opened: {filename[0]}')
            self._model.readImageGrayFile(filename[0])
            self._model.inputToOutput()
            self.showImage()

    def _saveFile(self):
        filename = QFileDialog.getSaveFileName(
            self._windowMain,
            'Select a File',
            '/Users/sudat/Documents/Notebooks/Project_PyOpenCV_PyQt5/assets',
            'Images (*.png *.jpg);;All (*)'
        )
        if filename:
            cv.imwrite(filename[0], self._model.getOutputImage())
            if os.path.isfile(filename[0]):
                self._windowMain.msgLabel.setText(f'File saved: {filename[0]}')

def main():
    app = QApplication(sys.argv)
    controller = Controller()
    app.exec()

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    main()