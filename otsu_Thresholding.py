# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otsu_Thresholding.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 58, 16))
        self.label.setObjectName("label")
        self.options = QtWidgets.QComboBox(Dialog)
        self.options.setGeometry(QtCore.QRect(130, 10, 251, 32))
        self.options.setObjectName("options")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 101, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 101, 16))
        self.label_3.setObjectName("label_3")
        self.slider_lower = QtWidgets.QSlider(Dialog)
        self.slider_lower.setGeometry(QtCore.QRect(140, 80, 231, 25))
        self.slider_lower.setMaximum(255)
        self.slider_lower.setOrientation(QtCore.Qt.Horizontal)
        self.slider_lower.setObjectName("slider_lower")
        self.slider_upper = QtWidgets.QSlider(Dialog)
        self.slider_upper.setGeometry(QtCore.QRect(140, 160, 231, 25))
        self.slider_upper.setMaximum(255)
        self.slider_upper.setProperty("value", 255)
        self.slider_upper.setOrientation(QtCore.Qt.Horizontal)
        self.slider_upper.setObjectName("slider_upper")
        self.label_lower = QtWidgets.QLabel(Dialog)
        self.label_lower.setGeometry(QtCore.QRect(150, 120, 58, 16))
        self.label_lower.setObjectName("label_lower")
        self.label_upper = QtWidgets.QLabel(Dialog)
        self.label_upper.setGeometry(QtCore.QRect(150, 190, 58, 16))
        self.label_upper.setObjectName("label_upper")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Otsu Thresholding"))
        self.label.setText(_translate("Dialog", "Options"))
        self.label_2.setText(_translate("Dialog", "lower threshold"))
        self.label_3.setText(_translate("Dialog", "higher threshold"))
        self.label_lower.setText(_translate("Dialog", "0"))
        self.label_upper.setText(_translate("Dialog", "255"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
