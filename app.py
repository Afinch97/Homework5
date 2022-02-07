import os

from flask import Flask, render_template
from tmdb import get_trending

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    
    return render_template(
        "index.html",
        
        )