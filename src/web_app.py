from flask import Flask, render_template, jsonify
from scraper import HNScraper
from filters import filter_more_than_five_words, filter_five_or_less_words
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
        try:
            scraper = HNScraper()
            entries = scraper.scrape()
            if not entries:
                logging.warning("No entries returned from scraper")
                return jsonify({"error": "No entries found"}), 404
            return jsonify(entries)
        except Exception as e:
             logging.error(f"Error in /scrape route: {e}")
             return jsonify({"error": str(e)}), 500

@app.route('/filter/more_than_five')
def filter_more():
    try:
        scraper = HNScraper()
        entries = scraper.scrape()
        if not entries:
            logging.warning("No entries returned from scraper")
            return jsonify({"error": "No entries found"}), 404
        filtered = filter_more_than_five_words(entries)
        return jsonify(filtered)
    except Exception as e:
         logging.error(f"Error in /filter/more_than_five route: {e}")
         return jsonify({"error": str(e)}), 500

@app.route('/filter/five_or_less')
def filter_less():
    try:
        scraper = HNScraper()
        entries = scraper.scrape()
        if not entries:
             logging.warning("No entries returned from scraper")
             return jsonify({"error": "No entries found"}), 404
        filtered = filter_five_or_less_words(entries)
        return jsonify(filtered)
    except Exception as e:
         logging.error(f"Error in /filter/five_or_less route: {e}")
         return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)