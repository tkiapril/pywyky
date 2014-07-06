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
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Wiki!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
