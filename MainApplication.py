from MainUI import Ui_MainWindow
import sys

from PyQt5.QtWidgets import (
    QMainWindow, QApplication
)

class MainApplication(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Setup UI
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    window = MainApplication()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
    
    