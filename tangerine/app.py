import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)


@app.route('/')
def typora():
    url = 'https://dev.to/blazephoenix/webscraping-in-python-with-flask-and-beautifulsoup-4-1pkl'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    r = requests.get(url, headers= headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    return render_template('index.html')
    title = soup.select_one('div.home> header.title> h1.medium')
    # temp_html = `<em>${title}</em>`
    

if __name__ == '__main__':
    app.run('0.0.0.0', port= 5000, debug= True)
