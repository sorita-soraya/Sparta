import requests
from bs4 import BeautifulSoup
import re

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
music = soup.select('#body-content > div > div > table>tbody>tr')

rank=0
for song in music:
    a_tag=song.select_one('td>a.title.ellipsis')
    if a_tag is not None:
        title=a_tag.text.replace(" ","")
        artist=song.select_one('td>a.artist.ellipsis').text.replace(" ","")
        rank+=1
        result = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
        print(rank,result,artist)
