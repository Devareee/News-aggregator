from PyQt5 import QtWidgets, uic


class FullWindow(QtWidgets.QMainWindow):
    def __init__(self, app, item, text):
        super(FullWindow, self).__init__()
        self.app = app
        uic.loadUi(self.app.ui_path.joinpath('full.ui'), self)
        self.label_2.setText(item)
        self.textBrowser.setText(text)
