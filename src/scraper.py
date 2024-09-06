import requests
from bs4 import BeautifulSoup

class HNScraper:
    def __init__(self , url="https://news.ycombinator.com/"):
        self.url = url

    def scrape(self, limit=30):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.praser")

        entries = []
        for item in soup.find_all('tr', class_='athing')[:limit]:
            rank = item.find('span', class_='rank').text.strip('.')
            title = item.find('a', class_='storylink').text

            subtext = item.find_next_sibling('tr').find('td', class_='subtext')
            points = subtext.find('span', class_='score').text.split()[0] if subtext.find('span', class_='score') else '0'
            comments =subtext.find_all('a')[-1].text.split()[0] if 'comment' in subtext.find_all('a')[-1].text else '0'

            entries.append({
                'rank': int(rank),
                'title': title,
                'points': int(points),
                'comments': int(comments) if comments.isdigit() else 0
            })

        return entries