from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/nse-data', methods=['GET'])
def get_nse_data():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/home/render/chrome/opt/google/chrome/google-chrome"

    service = Service("/home/render/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.nseindia.com/api/sectorIndices")
    data = driver.page_source
    driver.quit()

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
