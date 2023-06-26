from application import window
import pathlib
import sys
from PyQt5 import QtWidgets


class Agregator:
    def __init__(self):
        self.app_path = pathlib.Path(__file__).parent.resolve().joinpath('application')
        self.ui_path = self.app_path.joinpath('ui')
        self.app = QtWidgets.QApplication(sys.argv)
        self.window = window.Window(self)
        self.app.exec_()


if __name__ == '__main__':
    app = Agregator()
