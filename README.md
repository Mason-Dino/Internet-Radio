# Internet Radio

This is a very simple internet radio to play songs. This is my lesson plan for Interdisciplinary Coding (CSC-374). One of my Computer Science professors reach out and asked if I wanted to give a lesson and I was like why not and this is what I came up with. This is no where the most efficient path but it is a path that is possible. 

This project is meant for a linux based device like a raspberry pi. 

## Steps for Install

Make sure that python flask is installed on the device. 
```sh
sudo apt install python3-flask
```

## Get the IP
To get the IP of the raspberry pi device we need to run a command

```sh
ifconfig
```

you should see a segment called `wlan0` and around there you should find a `inet` which will have the ip of the device. 

## Code Environment


We will be using flask as the back end to serve as our little internet server, and then html and js will help with out front end. 

`Make sure that you are in the main directory or desktop directory`

```sh
mkdir music
```

Students should get mp3 files in this part and place them in the music directory. 

```sh
nano radio.py
```

The code below is going to be need. For the first 2 lines we are needing to import the library's that we need to complete this project

app var is going to help initiate the flask environment <br>
MUSIC var is just the dir for all of the music that we will use<br>
playlist array is going the array that stores all the music files

```py
from flask import Flask, Response, render_template
import os

app = Flask(__name__)
MUSIC = "/home/dsu/Desktop/music"
playlist = []
```

Next we will actually get the flask environment set up so we have a basic web server.

with the `app.route("/")` that is setting the url so when I go to the ip of the raspberry pi it will go to this code segment and then it will return `Hello World`

`Add this to the radio.py file`

```py
@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run("raspberrypi-ip", port=5000, debug=True)
```

Lets test out what we have right now to make sure that it works

Head to: `http://raspberrypi-ip:5000/` <br>
it should return `Hello World`

The next code segments are going to be spread out a little bit in relation to what we have just written. 

This code segments gets all the audio files within the music directory.

```py
#this is code will go right below playlist = []

for file in os.listdir(MUSIC):
    if file.endswith(".mp3"):
        playlist.append(file)
```

This code segment will make another url endpoint and will return the songs we have in playlist. This is an important step!

```py
# this segment of code will go under the index function

@app.route("/list")
def songList():
    return playlist
```

You `radio.py` file should look like the following

```py
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
    return playlist

if __name__ == "__main__":
    app.run(port=5000, debug=True)
```

Let check to make sure that this code all works

head to: `http://raspberrypi-ip:5000/list`<br>
return: `mp3 files you have in music directory`

We are going to add one more url endpoint and then we are going to be all done with adding url endpoints. 

this code segment first gets the song from the song url end point and then it goes to the generate function which gets the whole song directory to have the entire directory. It then reads the song in binary mode to get the correct data. it then assigns part of the file in the data variable and then returns some of the mp3 data and counties to do that until it reaches the end of the song. 

```py
#put this code right under the list function

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
```

Now it is time for the html part. We need to make another directory

```sh
mkdir template
cd template
```

Make sure that you are in the template directory so we can then make an index.html page

```sh
nano index.html
```

We need to get the basic html file outline put out

```html
<!DOCTYPE html>
<html>
    <head>

    </head>
    <body>

    </body>
</html>
```

Now that we have the basic html structure we need to actually start adding elements within the html code

Within the body tag add the following html code

This code creates a audio player within the html page with a source to `song.mp3 (replace this with an actual mp3 file)`

```html
<audio controls autoplay muted id="audioPlayer">
    <source src="/song/song.mp3" type="audio/mpeg">
</audio>
```