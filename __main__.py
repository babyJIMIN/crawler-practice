from itertools import count

from collection import crawler
from bs4 import BeautifulSoup

def crawling_pelicana():
    results = []

    for index in count(start=110, step=1):
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
            sidogu = address.split()[:2]

            # to tuple
            t = (name, address) + tuple(sidogu)
            results.append(t)

    # store

if __name__ == '__main__':
    crawling_pelicana()