from selenium import webdriver
from flask import Flask, request
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

app = Flask(__name__)

def download_selenium():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(" -- headless")
    chrome_options.add_argument(" -- nc-sandbox")
    chrome_options.add_argument(" -- disable-cev-she-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://google.com")
    title = driver.title
    language = driver.find_element (By.XPATH, "//div[@id='SIvCob']").text
    data = {'Page Title': title, 'Language': language}
    return data

@app.route('/', methods = ['GET','POST'])
def hame():
    if (request.method == 'GET'):
        return download_selenium()

if __name__ == "_main_":
    app.run(debug=True, port=3000)