import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
# 웹 브라우저 요청인 것처럼 위장하기 위해 아래 헤더를 추가해 요청
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',
    headers=headers
)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################

# > : 자식 태그
# :nth-child(n) : n번째 자식 태그
#old_content > table > tbody > tr:nth-child(2) > td.title > div > a
#old_content > table > tbody > tr:nth-child(3) > td.title > div > a

#old_content > table > tbody > tr:nth-child(2) > td.point


# tr 태그를 셀렉트
# select() -> 조건에 맞는 태그를 1개 이상 가져옴, 보통 반복문에서 사용할 수 있음
movies = soup.select('#old_content > table > tbody > tr')
for movie in movies:
    # select_one() -> 조건에 맞는 태그를 1개만 찾음, 없을 경우 None
    a_tag = movie.select_one('td.title > div > a')

    if a_tag is not None:  # a_tag 태그가 존재한다면
        rating = movie.select_one('td.point')
        print(a_tag.text)
        print(rating.text)
