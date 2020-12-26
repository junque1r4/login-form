from flask import Flask, render_template, redirect, session
from functools import wraps
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = b'<PUT-A-SECRET-KEY-HERE>'

try:
    client = MongoClient("<YOUR-DB-HERE>")
    db = client['project_login']
    print(' * Database Connected!')
except:
    print(' * Cannot connect to the database!')


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')

    return wrap


#* Routes
from user import routes

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('dashboard.html')
