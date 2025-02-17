from flask import Flask, Response, render_template
import os
import random

app = Flask(__name__)
MUSIC = "/home/dsu/Desktop/music"
playlist = []

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(port=5000, debug=True)