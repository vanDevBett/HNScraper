from flask import Flask, render_template, jsonify
from scraper import HNScraper
from filters import filter_more_than_five_words, filter_five_or_less_words

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    scraper = HNScraper()
    entries = scraper.scrape()
    return jsonify(entries)

@app.route('/filter/more_than_five')
def filter_more():
    scraper = HNScraper()
    entries = scraper.scrape()
    filtered = filter_more_than_five_words(entries)
    return jsonify(filtered)

@app.route('/filter/five_or_less')
def filter_less():
    scraper = HNScraper()
    entries = scraper.scrape()
    filtered = filter_five_or_less_words(entries)
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)