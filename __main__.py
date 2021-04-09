from itertools import count

from collection import crawler
from bs4 import BeautifulSoup
import pandas as pd
# from selenium import webdriver

def crawling_pelicana():
    results = []

    for index in count(start=1, step=1):
        url = f'https://pelicana.co.kr/store/stroe_search.html?page={index}&branch_name=&gu=&si='
        html = crawler.crawling(url)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class' : ['table', 'mt20']})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        if len(tags_tr) == 0:
            print("end of list " + str(index))
            break

        for tag_tr in tags_tr:
            datas = (list(tag_tr.strings))
            name = datas[1]
            address = datas[3]
            sidogugun = address.split()[:2]

            # to tuple
            t = (name, address) + tuple(sidogugun)
            results.append(t)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('results/pelicana.csv', encoding='utf-8', mode='w', index=True)

def crawling_nene():
    pass

def crawling_kyochon():
    pass

def crawling_goobne():
    # Chrome 브라우저 띄우기
    url = "http://goobne.co.kr/store/search_store.jsp"
    wd = webdriver.Chrome("C:\\Users\\izimi\\OneDrive\\바탕 화면\\수업자료\\(비트교육) 융복합 AI 응용서비스 개발 실무\\01_Python Web & DB\chromedriver_win32\\chromedriver")
    wd.get('https://www.google.com')

    # 페이지 이동
    wd.get(url)
    time.sleep(3)

    results = []

    # 자바 스크립트 실행
    # for index in count(start=1, step=1):
    for index in range(105, 200):
        script = f'store.getlist({index})'
        wd.execute_script(script)
        print(f'{datetime.now()} : success for request [{script}]')
        time.sleep(3)

        # 자바스크립트로 실행된 HTML(동적으로 렌더링된 HTML) 가져오기
        html = wd.page.source
        print(html)

        # 파싱(bs4)
        bs = BeautifulSoup(html, 'html.parser')
        tags_tbody = bs.find('tbody', attrs={'id':'store_list'})
        tags_tr = tags_tbody.findAll('tr')

        # 끝 검출
        if tags_tr[0].get('class') is None:
            break

        for tag_tr in tags_tr:
            datas = list(tag_tr.strings)
            name = datas[1]
            address = datas[6]
            sidogugun = address.split()[:2]

            t = (name, address) + tuple(sidogugun)
            results.append(t)

    print(results)

    # 브라우저 닫기
    wd.close()

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('results/goobne.csv', encoding='utf-8', mode='w', index=True)

if __name__ == '__main__':
    crawling_pelicana()
    # crawling_goobne()