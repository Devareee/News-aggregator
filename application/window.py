from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTimer
import json
from . import qt, full, parser


class Window(QtWidgets.QMainWindow):
    def __init__(self, app):
        super(Window, self).__init__()
        self.app = app
        uic.loadUi(self.app.ui_path.joinpath('news.ui'), self)
        self.setFixedSize(self.size())
        self.show()
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.update_time = 300000
        self.parser = parser.Parser(self)
        self.links_dict = {}
        with open(self.app.app_path.joinpath("links_dict.json")) as f:
            self.links_dict = json.load(f)
        for links in self.links_dict:
            self.parser.get_first_news(self.links_dict[links]["site_url"], self.links_dict[links]["article"],
                                       self.links_dict[links]["article_title"], self.links_dict[links]["article_text"],
                                       self.links_dict[links]["article_url"], self.links_dict[links]["title"],
                                       self.links_dict[links]["text"], self.links_dict[links]["num"])
        self.parser.check_double()
        with open(self.app.app_path.joinpath("news_dict.json")) as file:
            self.news_dict = json.load(file)
        for names in self.news_dict:
            qt.add_table_row(self.tableWidget, self.news_dict[names]["article_title"])
        self.tableWidget.setColumnWidth(0, 1020)
        self.tableWidget.cellClicked.connect(self.tableWidget_cellClicked)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_news)
        self.timer.start(self.update_time)

    def pushButton_2_clicked(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        with open(self.app.app_path.joinpath("news_dict.json")) as file:
            self.news_dict = json.load(file)
        for names in self.news_dict:
            qt.add_table_row(self.tableWidget, self.news_dict[names]["article_title"])
        try:
            if isinstance(int(self.lineEdit_2.text()), int):
                self.timer.stop
                self.update_time = int(self.lineEdit_2.text())*60*1000
                self.timer.start(self.update_time)
        except:
            pass

    def pushButton_clicked(self):
        search = self.lineEdit.text()
        search_news = {}
        if self.tableWidget.rowCount() == 0: return
        for i in range(self.tableWidget.rowCount()):
            name = self.tableWidget.item(i, 0).text()
            if name.lower().find(search.lower() + ' ') != -1 or name.lower().find(' ' + search.lower()) != -1:
                search_news[i] = {
                    "article_title": name,
                    "article_text": self.parser.get_article(name)
                }
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 1020)
        for names in search_news:
            qt.add_table_row(self.tableWidget, search_news[names]["article_title"])

    def tableWidget_cellClicked(self):
        item = self.tableWidget.currentItem()
        text = self.parser.get_article(item.text())
        self.full_window = full.FullWindow(self.app, item.text(), text)
        self.full_window.show()

    def update_news(self):
        for links in self.links_dict:
            self.parser.get_first_news(self.links_dict[links]["site_url"], self.links_dict[links]["article"],
                                       self.links_dict[links]["article_title"], self.links_dict[links]["article_text"],
                                       self.links_dict[links]["article_url"], self.links_dict[links]["title"],
                                       self.links_dict[links]["text"], self.links_dict[links]["num"])
        self.parser.check_double()
        with open(self.app.app_path.joinpath("news_dict.json")) as file:
            self.news_dict = json.load(file)
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for names in self.news_dict:
            qt.add_table_row(self.tableWidget, self.news_dict[names]["article_title"])
