import requests
from bs4 import BeautifulSoup

# url의 date 부분을 변경하면 원하는 날짜의 영화 조회가능
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20220127%22'
html = requests.get(url)
print(html.text)