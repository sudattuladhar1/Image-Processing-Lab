import numpy as np
import cv2 as cv

class Model():
    def __init__(self) -> None:
        self._inputImg = None
        self._outputImg = None

    def readImageFile(self, filename):
        self._inputImg = cv.imread(filename)

    def readImageGrayFile(self, filename):
        self._inputImg = cv.imread(filename, cv.IMREAD_GRAYSCALE)

    def inputToOutput(self):
        self._outputImg = self._inputImg

    def outputToInput(self):
        self._inputImg = self._outputImg

    def getOutputImage(self):
        return self._outputImg
    
    def invertImage(self):
        self._outputImg = cv.bitwise_not(self._inputImg)

    def toGrayScale(self):
        self._outputImg = cv.cvtColor(self._inputImg, cv.COLOR_BGR2GRAY)

    def gaussianBlur(self, kernel_size, borderType):
        self._outputImg = cv.GaussianBlur(
                self._inputImg, 
                (kernel_size, kernel_size), 
                sigmaX=0,
                sigmaY=None,
                borderType=borderType
        )

    def otsuThresholding(self, lower, upper, method):
        _, self._outputImg = cv.threshold(self._inputImg, lower, upper, method)

    