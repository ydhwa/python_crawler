import ssl
import sys
from datetime import datetime
from itertools import count
from urllib.request import Request, urlopen

import pandas as pd
from bs4 import BeautifulSoup


def crawling_pelicana():
    results = []

    for page in count(start=1):
        url = 'https://pelicana.co.kr/store/stroe_search.html?page=%d&branch_name=&gu=&si=' % page
        try:
            request = Request(url)

            ssl._create_default_https_context = ssl._create_unverified_context
            response = urlopen(request)

            receive = response.read()
            html = receive.decode('utf-8', errors='replace')

            print(f'{datetime.now()}: success for request [{url}]')
        except Exception as e:
            # datetime import 주의
            print(f'{e}: {datetime.now()}', file=sys.stderr)
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


if __name__ == '__main__':
    # pelicana
    # crawling_pelicana()

    # nene 과제
    crawling_nene()