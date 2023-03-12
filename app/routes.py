#!/usr/bin/env python3
#_*_ coding: utf8 _*_
"""FSDI-111 Assignment 2"""


from flask import Flask

app = Flask(__name__)


@app.get("/")
def about_me():
    me = {
        "first_name": "Scott",
        "last_name": "Stevens",
        "hobbies": "Flying Drones",
        "active": True    
    }

    return me
