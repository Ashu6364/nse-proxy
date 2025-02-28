from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/nse-data', methods=['GET'])
def get_nse_data():
    url = "https://www.nseindia.com/api/sectorIndices"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Referer": "https://www.nseindia.com/"
    }
    response = requests.get(url, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # Render uses ports above 10000
