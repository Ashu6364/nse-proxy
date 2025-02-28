#!/bin/bash

# Install Chrome
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -x google-chrome-stable_current_amd64.deb $HOME/chrome
export PATH=$HOME/chrome/opt/google/chrome:$PATH

# Get latest ChromeDriver version dynamically
CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget -q "https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip"

# Extract ChromeDriver
unzip chromedriver_linux64.zip
chmod +x chromedriver
mv chromedriver $HOME/chromedriver

# Set environment variables
export PATH=$HOME:$PATH
export DISPLAY=:99

# Run Flask app
python3 proxy.py
