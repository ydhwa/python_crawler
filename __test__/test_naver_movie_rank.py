import re
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

from collection import crawler


def ex01():
    request = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    response = urlopen(request)
    # [페이지 소스 보기] 에서 charset 확인. euc-kr 인데, 이를 파이썬에서는 cp949라 함
    html = response.read().decode('cp949')
    # print(html)

    bs = BeautifulSoup(html, 'html.parser')
    # print(bs.prettify())        # 더 예쁘게 보여줌

    divs = bs.findAll('div', attrs={'class': 'tit3'})
    # print(divs)

    for index, div in enumerate(divs):
        print(index + 1, div.a.text, div.a['href'], sep=": ")
    print('======================================')


def proc_naver_movie_rank(html):
    # processing
    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    return divs


def store_naver_movie_rank(data):
    # output(store)
    for index, div in enumerate(data):
        print(index + 1, div.a.text, div.a['href'], sep=": ")


def ex02():
    # fetch
    result = crawler.crawling(url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn', encoding='cp949',
                              proc1=proc_naver_movie_rank,
                              proc2=lambda data: list(map(lambda x: print(x.a.text, x.a['href'], sep=": "), data)))


# ex01()이 None을 return해주므로 and not을 조건으로 걸어야 뒤에 있는 ex02()가 실행된다.
__name__ == '__main__' and not ex01() and not ex02()
