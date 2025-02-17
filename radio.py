from flask import Flask, Response, render_template
import os
import random

app = Flask(__name__)
MUSIC = "/home/dsu/Desktop/music"
playlist = []

