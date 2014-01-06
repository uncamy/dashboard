import os
import sqlite3
import string
import pandas as pd

#from geopy.geocoders import GoogleV3
#import geopy.distance
#from googlemap import GoogleMaps
#import api_key.py


from flask  import Flask, request, session, g, redirect, url_for,\
                  abort, render_template, flash, json

#configuration
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
