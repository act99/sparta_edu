import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select("#body-content > div.newest-list > div > table > tbody > tr")
for tr in trs:
    rank_unrefined = tr.select_one("td.number")
    details_unrefined = tr.select_one("td.info")
    details_title = details_unrefined.select_one("a.title.ellipsis").text.strip()
    details_artist = details_unrefined.select_one("a.artist.ellipsis").text.strip()
    for tag in rank_unrefined.find_all("span", {"class": "rank"}):
        tag.replaceWith("")
    rank = rank_unrefined.text.strip()

    doc = {
        "rank": rank,
        "title": details_title,
        "artist": details_artist
    }
    db.songs.insert_one(doc)
    print(rank,details_title,details_artist)
