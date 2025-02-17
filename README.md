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