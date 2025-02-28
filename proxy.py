from flask import Flask, jsonify
import cloudscraper

app = Flask(__name__)

@app.route('/nse-data', methods=['GET'])
def get_nse_data():
    url = "https://www.nseindia.com/api/sectorIndices"
    
    # Use cloudscraper to bypass Cloudflare protection
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
