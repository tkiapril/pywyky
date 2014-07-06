#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# pywyky: a simple wikiwiki based on Python 3.4 and Flask
# by Tki April
#
# wiki.py: the main executable script
# added on 2014-07-07
#

from flask import Flask
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient()
db = client.pywyky

@app.route("/")
def hello():
    return db.documents.find_one({"title": "대문"})["content"]

if __name__ == "__main__":
    app.run(host='0.0.0.0")
