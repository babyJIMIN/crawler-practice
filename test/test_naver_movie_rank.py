import os
import sys

try:
    # sys.path.append(os.getcwd())
    sys.path.append('C:/Users/izimi/OneDrive/바탕 화면/수업자료/(비트교육) 융복합 AI 응용서비스 개발 실무/01_Python Web & DB/vscode/crawler-practice')
except ImportError:
    raise ImportError("Import Fail")


from urllib.request import Request, urlopen
from collection import crawler
from bs4 import BeautifulSoup

def ex01():
    request = Request("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
    response = urlopen(request)
    html = response.read().decode('cp949')

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    for div in divs:
        print(div.a.text)

def ex02():
    html = crawler.crawling("https://movie.naver.com/movie/sdb/rank/rmovie.nhn", 'cp949')

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    for index, div in enumerate(divs):
        print(index+1, div.a.text, div.a['href'], sep=' : ')


if __name__ == '__main__':
    # ex01()
    ex02()