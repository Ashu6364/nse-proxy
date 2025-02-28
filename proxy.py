from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)

@app.route('/nse-data', methods=['GET'])
def get_nse_data():
    options = Options()
    options.add_argument("--headless")  # Run without UI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Use correct ChromeDriver path for Render
    service = Service("/usr/local/bin/chromedriver")

    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.nseindia.com/api/sectorIndices")
        data = driver.page_source
        driver.quit()
        return jsonify({"data": data})
    except Exception as e:
        driver.quit()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
