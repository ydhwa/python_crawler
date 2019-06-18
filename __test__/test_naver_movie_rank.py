import re
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

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