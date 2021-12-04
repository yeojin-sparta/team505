import requests
from bs4 import BeautifulSoup

# test
def print_song(date, rate):
    """특정 날짜의 특정 순위 곡을 출력한다

    :param date: 날짜('01'~'31')
    :param rate: 순위(1~50)
    :return:
        프린트해줌
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # in python(f-string)!
    url = f'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=202111{date}'

    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

    first_song = songs[rate - 1]  # songs 타입이 리스트 형식이기 때문에 첫 번째 곡만 가져온다
    a_tag = first_song.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        print(a_tag.text.strip())


rate = 49
date_list = ['01', '02', '03', '04', '05']
for date in date_list:
    print(f'{date}일의 {rate}위곡은?')
    print_song(date, rate)
