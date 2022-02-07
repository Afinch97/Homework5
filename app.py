import os

from flask import Flask, render_template
from tmdb import get_trending

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    data = get_trending()
    
    return render_template(
        "index.html",
        titles = data['titles'],
        overviews = data['overviews'],
        posters = data['posters'],
        )
    
app.run(
    host=os.getenv('IP','0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug = True
)