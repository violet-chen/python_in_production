import sys
from PySide2 import QtWidgets

class StandaloneWindow(QtWidgets.QWidget):

    def __init__(self):
        super(StandaloneWindow, self).__init__(parent=None)

        self.setWindowTitle("Standalone App")
        self.setMinimumSize(400, 300)

        self.close_btn = QtWidgets.QPushButton("Close", self)
        self.close_btn.clicked.connect(self.close)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = StandaloneWindow()
    window.show()

    app.exec_()