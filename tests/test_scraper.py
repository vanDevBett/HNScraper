import pytest
from src.scraper import HNScraper

def test_scraper():
    scraper = HNScraper()
    entries = scraper.scrape(limit=5)
    assert len(entries) == 5
    for entry in entries:
        assert 'rank' in entry
        assert 'title' in entry
        assert 'points' in entry
        assert 'comments' in entry