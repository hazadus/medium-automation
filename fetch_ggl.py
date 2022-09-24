"""
Fetch Google Search

pip install beautifulsoup4
pip install requests
"""

import requests

from bs4 import BeautifulSoup


def google_search(query: str, max_results: int) -> dict:
    url = f"https://www.google.com/search?q={query}&num={max_results}"
    req = requests.get(url)
    html = BeautifulSoup(req.content, "html.parser")
    links = html.find_all("a")
    results = dict()

    for result in links:
        href = result.get('href')
        if "url?q=" in href and not "webcache" in href:
            title = result.find_all('h3')
            if len(title) != 0:
                url = result.get('href')
                url = url.split("&")[0]
                url = url.split("url?q=")[1]
                results.update({title[0].text: url})
    return results


if __name__ == '__main__':
    found = google_search('best python tutorials', 10)
    print('\n'.join([title + ' ' + link for title, link in found.items()]))
