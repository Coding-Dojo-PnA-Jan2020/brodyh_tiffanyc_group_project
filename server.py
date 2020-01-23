# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, flash, session
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL

app = Flask(__name__)


# Definitions go here

if __name__ == '__main__':
    app.run(debug = True)