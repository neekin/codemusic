from datetime import datetime
from flask import render_template,session,redirect,url_for,flash

from . import main
# from .forms import NameForm
from .. import db

@main.route('/')
def index():
    return render_template('index.html')    