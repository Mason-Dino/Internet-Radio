# Internet Radio

This is a very simple internet radio to play songs. This is my lesson plan for Interdisciplinary Coding (CSC-374). One of my Computer Science professors reach out and asked if I wanted to give a lesson and I was like why not and this is what I came up with. This is no where the most efficient path but it is a path that is possible. 

This project is meant for a linux based device like a raspberry pi. 

## Steps for Install

Make sure that python flask is installed on the device. 
```sh
sudo apt install python3-flask
```

## Code Environment


We will be using flask as the back end to serve as our little internet server, and then html and js will help with out front end. 

`Make sure that you are in the main directory or desktop directory`

```sh
mkdir music
```

```sh
nano radio.py
```

```py
from flask import Flask, Response, render_template
import os

app = Flask(__name__)
MUSIC = "/home/dsu/Desktop/music"
playlist = []
```