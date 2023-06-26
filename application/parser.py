import requests
import textdistance as td
from bs4 import BeautifulSoup
import json


class Parser():
    def __init__(self, app):
        self.app = app
        self.news_dict = {}
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

    def get_first_news(self, url, ar, artit, artext, arurl, title, text, num):
        code = 429
        while code == 429:
            r = requests.get(url=url, headers=self.headers)
            code = r.status_code
        soup = BeautifulSoup(r.text, "lxml")
        articles_cards = soup.find_all("div", class_=ar)
        for article in articles_cards:
            try:
                article_url = article.find("a", class_=arurl).get("href")
                article_title = article.find(title, class_=artit).text.strip()
                article_text = article.find(text, class_=artext).text.strip()
                if article_text == "":
                    continue
                article_id = article_url.split('/')[-int(num)]
                if article_id in self.news_dict:
                    continue
                self.news_dict[article_id] = {
                    "article_title": article_title,
                    "article_text": article_text
                }
            except AttributeError:
                pass
            except UnicodeEncodeError:
                pass

        with open("application/news_dict.json", "w") as file:
            json.dump(self.news_dict, file, indent=4, ensure_ascii=True)

    def check_news_update(self, url, ar, artit, artext, arurl, title, text, num):
        code = 429
        while code == 429:
            r = requests.get(url=url, headers=self.headers)
            code = r.status_code
        soup = BeautifulSoup(r.text, "lxml")
        articles_cards = soup.find_all("div", class_=ar)
        for article in articles_cards:
            try:
                article_url = article.find("a", class_=arurl).get("href")
                article_id = article_url.split('/')[-int(num)]
                if article_id in self.news_dict:
                    continue
                article_title = article.find(title, class_=artit).text.strip()
                article_text = article.find(text, class_=artext).text.strip()
                if article_text == "":
                    continue
                self.news_dict[article_id] = {
                    "article_title": article_title,
                    "article_text": article_text
                }
            except AttributeError:
                pass
        with open("application/news_dict.json", "w") as file:
            json.dump(self.news_dict, file, indent=4, ensure_ascii=True)

    def get_article(self, article_title):
        for names in self.news_dict:
            if str(self.news_dict[names]["article_title"]) == str(article_title):
                return self.news_dict[names]["article_text"]

    def check_double(self):
        delete = {}
        for names in self.news_dict:
            for names2 in self.news_dict:
                if (td.sorensen.normalized_similarity(str(self.news_dict[names]["article_title"]), str(self.news_dict[names2]["article_title"])) >= 0.85 and
                td.sorensen.normalized_similarity(str(self.news_dict[names]["article_title"]), str(self.news_dict[names2]["article_title"])) < 1):
                    delete[names] = {
                        "article_title": self.news_dict[names]["article_title"],
                        "article_text": self.news_dict[names]["article_text"]
                    }
        for dele in delete:
            print(dele)
            self.news_dict.pop(dele)
        with open("application/news_dict.json", "w") as file:
            json.dump(self.news_dict, file, indent=4, ensure_ascii=True)
