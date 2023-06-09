# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blurGaussian.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(403, 198)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 81, 16))
        self.label_2.setObjectName("label_2")
        self.blurGaussianBorderTypecomboBox = QtWidgets.QComboBox(Dialog)
        self.blurGaussianBorderTypecomboBox.setGeometry(QtCore.QRect(120, 20, 211, 32))
        self.blurGaussianBorderTypecomboBox.setObjectName("blurGaussianBorderTypecomboBox")
        self.blurGaussianKernelSizespinBox = QtWidgets.QSpinBox(Dialog)
        self.blurGaussianKernelSizespinBox.setGeometry(QtCore.QRect(120, 70, 42, 22))
        self.blurGaussianKernelSizespinBox.setMinimum(3)
        self.blurGaussianKernelSizespinBox.setMaximum(55)
        self.blurGaussianKernelSizespinBox.setSingleStep(2)
        self.blurGaussianKernelSizespinBox.setObjectName("blurGaussianKernelSizespinBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gaussian Blur"))
        self.label.setText(_translate("Dialog", "Border Type"))
        self.label_2.setText(_translate("Dialog", "Kernel Size"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
