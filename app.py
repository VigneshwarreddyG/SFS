from flask import Flask, render_template, request, redirect, url_for,session
from flask_mysql_connector import MySQL
import mysql.connector
import MySQLdb.cursors
app = Flask(__name__, static_url_path='/static')
import re
app.secret_key = 'your secret key'
from flask_mysqldb import MySQL
# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vigneshwar@94'
app.config['MYSQL_DB'] = 'login'
mysql = MySQL(app)
@app.route('/',methods=['POST','GET'])
def index():
    cursor =  mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM accounts")
    users = cursor.fetchall()
    cursor.close()
    return render_template('main.html', users=users)

@app.route('/customerlogin', methods =['GET', 'POST'])
def customerlogin():
    msg = ''
    print(request.method)
    print(request.form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('Custlogin.html', msg = msg)

@app.route('/customerregister', methods =['GET', 'POST'])
def Customerregister():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor =  mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute("INSERT INTO accounts (username, email,password) VALUES (%s, %s,%s)", (username, email,password))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            return render_template('Custlogin.html', msg = msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('Custregister.html', msg = msg)
if __name__ == '__main__':
    app.run(debug=True)


@app.route('/agentlogin', methods =['GET', 'POST'])
def agentlogin():
    msg = ''
    print(request.method)
    print(request.form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM agent_accounts WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('Agentlogin.html', msg = msg)


@app.route('/agentregister', methods =['GET', 'POST'])
def Agentregister():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor =  mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM agent_accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute("INSERT INTO agent_accounts (username, email,password) VALUES (%s, %s,%s)", (username, email,password))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            return render_template('Agentlogin.html', msg = msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('Agentregister.html', msg = msg)

@app.route('/adminlogin', methods =['GET', 'POST'])
def adminlogin():
    msg = ''
    print(request.method)
    print(request.form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admin WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('Adminlogin.html', msg = msg)

if __name__ == '__main__':
    app.run(debug=True)
