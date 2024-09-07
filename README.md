# HN Scraper

This project is a web crawler that scrapes the first 30 entries from Hacker News (https://news.ycombinator.com/) and provides filtering capabilities.

## Features

- Scrapes the first 30 entries from Hacker News
- Filters entries with more than five words in the title, ordered by number of comments
- Filters entries with five or fewer words in the title, ordered by points
- Web interface for easy interaction

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/hn-scraper.git
cd hn-scraper

2. Create a virtual environment and activate it:

For macOS and Linux:
python3 -m venv venv
source venv/bin/activate

For Windows:
python -m venv venv
venv\Scripts\activate

3. Install the requirements:
pip install -r requirements.txt

## Usage

1. Start the web application:

For macOS and Linux:
python src/web_app.py

For Windows:
python src\web_app.py

2. Open a web browser and navigate to http://localhost:5000

3. Use the provided buttons to scrape Hacker News and apply filters

## Running Tests

To run the automated tests:

For macOS and Linux:
pytest

For Windows:
python -m pytest
