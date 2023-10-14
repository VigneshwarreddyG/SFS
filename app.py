# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysql_connector import MySQL  # Flask extension for MySQL
import mysql.connector  # MySQL connector for database connection
import MySQLdb.cursors  # MySQLdb cursors for database interaction
import re  # Regular expressions for validation

# Create a Flask application
app = Flask(__name__, static_url_path='/static')

# Set a secret key for session management
app.secret_key = 'your_secret_key'

# Configure the MySQL connection settings
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Vigneshwar@94'
app.config['MYSQL_DB'] = 'login'

# Initialize the MySQL extension with Flask
mysql = MySQL(app)

# Route for the home page
@app.route('/', methods=['POST', 'GET'])
def index():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM accounts")
    users = cursor.fetchall()
    cursor.close()
    return render_template('main.html', users=users)

# Route for customer login
@app.route('/customerlogin', methods=['GET', 'POST'])
def customerlogin():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully!'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password!'
    return render_template('Custlogin.html', msg=msg)

# Route for customer registration
@app.route('/customerregister', methods=['GET', 'POST'])
def customerregister():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            cursor.execute("INSERT INTO accounts (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            return render_template('Custlogin.html', msg=msg)
    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('Custregister.html', msg=msg)

# Continue with the routes for agent login, agent registration, and admin login here...

if __name__ == '__main__':
    app.run(debug=True)
