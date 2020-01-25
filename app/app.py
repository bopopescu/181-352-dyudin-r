from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
application = app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/seepage')
def seepage():
  return render_template('seepage.html')