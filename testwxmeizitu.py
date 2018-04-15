import requests
import json
from bs4 import BeautifulSoup


url = 'https://mp.weixin.qq.com/s/GEfQUt0ayIulxnovYIa7eA'

r = requests.get(url, verify=False)
soup = BeautifulSoup(r.text, "lxml")
imgs = soup.find(id="js_content").find_all("img")
for img in imgs:
    print(img['data-src'])