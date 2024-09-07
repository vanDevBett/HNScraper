import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)

class HNScraper:
    def __init__(self , url="https://news.ycombinator.com/"):
        self.url = url

    def scrape(self, limit=30):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.praser")

            entries = []
            items = soup.find_all('tr', class_='athing')
            for item in items[:limit]:
                try:
                    rank_elem = item.find('span', class_='rank')
                    title_elem = item.find('span', class_='titleline').find('a')
                    subtext = item.find_next_sibling('tr').find('td', class_='subtext')

                    if rank_elem is None or title_elem is None or subtext is None:
                        logging.warning(f"Missing elements for item {item.get('id')}")
                        continue

                    rank = rank_elem.text.strip('.')
                    title = title_elem.text

                    score_elem = subtext.find('span', class_='score')
                    points = score_elem.text.split()[0] if score_elem else '0'

                    comment_elem = subtext.find('a', string=lambda text: 'comment' in text.lower() if text else False)
                    comments = comment_elem.text.split()[0] if comment_elem else '0'

                    entries.append({
                        'rank': int(rank),
                        'title': title,
                        'points': int(points),
                        'comments': int(comments) if comments.isdigit() else 0
                    })
                    logging.info(f"Processed entry: {title}")
                except AttributeError as e:
                    logging.error(f"AttributeError processing entry: {e}")
                except Exception as e:
                    logging.error(f"Unexpected error processing entry: {e}")
            
            logging.info(f"Scraped {len(entries)} entries")
            return entries
        except requests.RequestException as e:
            logging.error(f"Error fetching data: {e}")
            return []
        except Exception as e:
            logging.error(f"Unexpected error: [e]")
            return[]