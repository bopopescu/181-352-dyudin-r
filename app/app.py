from flask import Flask, render_template, url_for, redirect,request
import mysql.connector
import flask_login
from config import *


app = Flask(__name__)
application = app

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.session_protection = "strong"


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/signup',methods=['GET','POST'])
def signup():
  cnx = mysql.connector.connect(**cg)
  cursor = cnx.cursor(named_tuple=True)

  login = request.form.get('login')
  password = request.form.get('password')
  name = request.form.get('name')
  role = request.form.get('role')
  data = (login, password,name,role)

  if login and password:
    query = '''INSERT INTO `user`(`login`, `password`,`name`,`role`) 
               VALUES (%s,%s,%s,%s)'''
    cursor.execute(query, data)
    cnx.commit()
    return redirect(url_for('index'))
  cursor.close()
  cnx.close()

  return render_template('signup.html')


@app.route('/seepage')
def seepage():
  cnx = mysql.connector.connect(**cg)
  cursor = cnx.cursor(named_tuple=True)
  cursor.execute('select * from `appeal`')
  db = cursor.fetchall()
  cursor.close()
  cnx.close()
  return render_template('seepage.html',db=db)


@app.route('/edit',methods=['GET','POST'])
def edit():
  cnx = mysql.connector.connect(**cg)
  cursor = cnx.cursor(named_tuple=True)

  login = request.form.get('login')
  password = request.form.get('password')
  data = (login,password)
  query = 'select * from `user` where login=%s and password=%s'
  cursor.execute(query,data)
  user = cursor.fetchall()

  
  cursor.execute('select * from `appeal`')
  massivedb = cursor.fetchall()

  return render_template('edit.html')