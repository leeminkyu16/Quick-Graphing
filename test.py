import sys
from windowmain import WindowMain
import matplotlib

from PyQt5 import QtCore, QtWidgets

from windowregression import WindowLinearRidgeRegression        

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Test Application")

        window_main = WindowMain()

        self.setCentralWidget(window_main)

        self.show()

def main() -> None:
    matplotlib.use("Qt5Agg")

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    app.exec_()


if __name__ == "__main__":
    main()