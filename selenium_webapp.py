from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from flask import Flask, request
import os
import subprocess

print("CHROME VERSION:", subprocess.getoutput("chromium --version"))
print("CHROMEDRIVER VERSION:", subprocess.getoutput("chromedriver --version"))

app = Flask(__name__)

def download_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium"


    # Use system-installed ChromeDriver
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://google.com")
    title = driver.title
    language = driver.find_element(By.XPATH, "//div[@id='SIvCob']").text
    driver.quit()

    return {'Page Title': title, 'Language': language}

@app.route('/', methods=['GET', 'POST'])
def hame():
    if request.method == 'GET':
        return download_selenium()

# Fix main block
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
