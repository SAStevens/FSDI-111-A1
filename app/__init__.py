#!/usr/bin/env python3
#_*_ coding: utf8 _*_
"""FSDI-111 Assignment 1"""

from flask import Flask

app = Flask(__name__)

@app.route("/aboutme")
def aboutMe():
    return "h1><ul><li>First Name: Scott</li><li>Last Name: Stevens</li><li>Hobbies: Flying Drones</li></ul></h1>"
