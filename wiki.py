#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# pywyky: a simple wikiwiki based on Python 3.4 and Flask
# by Tki April
#
# wiki.py: the main executable script
# added on 2014-07-07
#

from flask import Flask, redirect, url_for
from pymongo import MongoClient
from markdown import markdown
import os, json
config = json.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")))
app = Flask(__name__)
client = MongoClient(config["database"]["server"], config["database"]["port"])
db = client[config["database"]["db"]]

@app.route("/")
@app.route("/wiki")
@app.route("/wiki/")
def index():
    return redirect('/wiki/대문')

@app.route("/wiki/<article_title>")
def show_article(article_title):
    article = db.articles.find_one({"title": article_title})
    if article:
        return markdown(article_title + "\n======\n\n" + article["content"])
    else:
        return "This page does not exist. You can create or search the page you wanted to find."

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=config["misc"]["debug"])
