from itertools import count

import pandas as pd
from bs4 import BeautifulSoup

from collection import crawler


def crawling_pelicana():
    results = []

    for page in count(start=1):
        url = 'https://pelicana.co.kr/store/stroe_search.html?page=%d&branch_name=&gu=&si=' % page
        try:
            html = crawler.crawling(url)
        except Exception as e:
            continue

        bs = BeautifulSoup(html, 'html.parser')

        tag_table = bs.find('table', attrs={'class': 'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[:2]

            results.append((name, address) + tuple(sidogu))

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('__results__/pelicana.csv', encoding='utf-8', mode='w', index=True)


def crawling_nene():
    results = []
    first_shopname = ''

    for page in count(start=1):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?ex_select=1&ex_select2=&IndexSword=&GUBUN=A&page=%d' % page
        try:
            html = crawler.crawling(url)
        except Exception as e:
            continue

        bs = BeautifulSoup(html, 'html.parser')

        # tag_table = bs.find('table', attrs={'class': 'shopTable'})
        tag_div_shopname = bs.findAll('div', attrs={'class': 'shopName'})
        tag_div_shopadd = bs.findAll('div', attrs={'class': 'shopAdd'})

        # 끝 검출
        if first_shopname == tag_div_shopname[0].text:
            break
        first_shopname = tag_div_shopname[0].text

        for i in range(len(tag_div_shopname)):
            name = tag_div_shopname[i].text
            address = tag_div_shopadd[i].text
            sidogu = address.split()[:2]

            results.append((name, address) + tuple(sidogu))

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('__results__/nene.csv', encoding='utf-8', mode='w', index=True)


def crawling_kyochon():
    results = []
    for sido1 in range(1, 18):
        for sido2 in count(1):
            url = 'http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' % (sido1, sido2)

            html = crawler.crawling(url)
            if html is None:
                break

            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul', attrs={'class': 'list'})
            tags_span = tag_ul.findAll('span', attrs={'class': 'store_item'})

            for tag_span in tags_span:
                strings = list(tag_span.strings)

                name = strings[1]
                address = strings[3].strip()
                sidodu = address.split()[:2]

                results.append((name, address) + tuple(sidodu))

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gugun'])
    table.to_csv('__results__/kyochon.csv', encoding='utf-8', mode='w', index=True)


if __name__ == '__main__':
    # pelicana
    # crawling_pelicana()

    # nene 과제
    # crawling_nene()

    # kyochon
    crawling_kyochon()
