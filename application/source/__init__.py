from flask import Flask
app=Flask(__name__)
#app._static_folder = "/home/ubuntu/app_demo/flaskexample/static"
app._static_folder = "/Users/ctoews/Documents/Insight/Project/poeml/application/source/static"
from source import views
