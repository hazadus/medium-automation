"""
Fetch Google Search

pip install beautifulsoup4
pip install requests
"""

import requests

from bs4 import BeautifulSoup

query = "цены на капусту в санкт-петербурге"
url = f"https://www.google.com/search?q={query}&num=10"
req = requests.get(url)
html = BeautifulSoup(req.content, "html.parser")
links = html.find_all("a")

for result in links:
    href = result.get('href')
    if "url?q=" in href and not "webcache" in href:
        title = result.find_all('h3')
        if len(title) != 0:
            url = result.get('href')
            url = url.split("&")[0]
            url = url.split("url?q=")[1]
            print(url)
            print(title[0].text)
            print("------")
