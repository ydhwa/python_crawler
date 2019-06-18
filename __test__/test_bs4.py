from bs4 import BeautifulSoup

html = '''<td class="title black">
<div class="tit3">
<a href="/movie/bi/mi/basic.nhn?code=161967" title="기생충">기생충</a>
</div>
</td>'''


# 1. tag 조회
def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    # print(bs)
    # print(type(bs))

    tag = bs.a
    # print(tag)
    # print(type(tag))

    tag = bs.td.div
    print(tag)
    print(type(tag))


# 2. attribute 값 가져오기
def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])     # 클래스가 여러 개 일 수 있어서

    # 없는 것을 가져오면 에러 발생
    # print(tag['id'])

    print(tag.attrs)


# 3. attribute로 조회
def ex3():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.find('td', attrs={'class': 'title'})
    print(tag, type(tag))

    tag = bs.find(attrs={'class': 'tit3'})
    print(tag)


if __name__ == '__main__':
    # ex1()
    # ex2()
    ex3()