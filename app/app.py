from flask import Flask, render_template, url_for, redirect,request
import mysql.connector
import flask_login
# from config import * не работает


app = Flask(__name__)
application = app
cg = {
    'user': 'std_879',
    'password': 'Logati22',
    'host': 'std-mysql.ist.mospolytech.ru',
    'database': 'std_879',
    'raise_on_warnings': True
}

@app.route('/')
def index():
  
  return render_template('index.html')


@app.route('/signup',methods=['GET','POST'])
def signup():
  cnx = mysql.connector.connect(**cg)
  cursor = cnx.cursor(named_tuple=True)

  username = request.args.get('username')
  password = request.args.get('password')
  name = request.args.get('name')
  role = request.args.get('role')
  data = (username, password,name,role)

  if username and password:
    query = '''INSERT INTO `user`(`username`, `password`,`name`,`role`) 
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