from flask import Flask, Response, render_template
import os

app = Flask(__name__)
MUSIC = "/home/dsu/Desktop/music"
playlist = []

for file in os.listdir(MUSIC):
    if file.endswith(".mp3"):
        playlist.append(file)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list")
def list():
    return {0: playlist}

def generate(song):
    song = os.path.join(MUSIC, song)
    print(song)
    with open(song, "rb") as f:
        data = f.read()
        while data:
            yield data
            data = f.read()
            
@app.route("/song/<song>")
def song(song):
    return Response(generate(song), mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(port=5000, debug=True)