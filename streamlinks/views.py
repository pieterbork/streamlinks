from flask import render_template, request, abort
from bs4 import BeautifulSoup
import requests

from . import app, db
from .models import Video

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stream')
def stream():
    vid_id = int(request.args.get('id', ''))
    vid = Video.query.filter(Video.id == vid_id).first()
    stream = vid.url

    return render_template('stream.html', stream=stream), 200

@app.route('/search', methods=['POST'])
def search():
    vids = []
    query = request.form['query']
    query_url = "https://www.youtube.com/results?search_query=" + query
    response = requests.get(query_url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        url = 'https://www.youtube.com' + link['href']
        if not 'watch' in url:
            continue
        print(url)

        vid = Video.query.filter(Video.link == url).first()
        if not vid:
            vid = Video(url)
            db.session.add(vid)
            db.session.commit()
        vids.append(vid)

    return render_template('results.html', vids=vids)
