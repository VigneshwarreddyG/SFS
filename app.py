from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import re

app = Flask(__name__)

# MySQL configuration
mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vigneshwar@94",
    database="SFS"
)
@app.route('/',methods=['POST','GET'])
def index():
    cursor =  mysql.cursor()
    cursor.execute("SELECT * FROM accounts")
    users = cursor.fetchall()
    cursor.close()
    return render_template('main.html', users=users)

@app.route('/Custregisterhtml',methods=['POST','GET'])
def Custregisterhtml():
    return render_template('Custregister.html')
@app.route('/Custloginhtml',methods=['POST','GET'])
def Custloginhtml():
    return render_template('Custlogin.html')
@app.route('/Ageloginhtml',methods=['POST','GET'])
def Agentloginhtml():
    return render_template('Agentlogin.html')
@app.route('/Ageregisterhtml',methods=['POST','GET'])
def Ageregisterhtml():
    return render_template('Agentregister.html')

@app.route('/Admin',methods=['POST','GET'])
def Adminlogin():
    return render_template('Adminlogin.html')


@app.route('/customerlogin', methods =['GET', 'POST'])
def customerlogin():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND pass = %s', (username, password))
        account = cursor.fetchone()
        cursor.close()
        print(account,"Hello 123789")
        if account:
            if account[7] != 'customer':
                return render_template('Custlogin.html', alert="Please login as a Customer to access this page!")
            if username == account[3] and password == account[6]:
                msg = 'Logged in successfully !'
                return render_template('index.html', msg = msg)
            else:
                msg = 'Incorrect username / password !'
                return render_template('Custlogin.html', msg = msg)
        else:
            return render_template('main.html',msg='Username or Password is incorrect!')

@app.route('/customerregister', methods =['GET', 'POST'])
def customerregister():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'fname' in request.form  and 'lname' in request.form and 'email' in request.form and 'phone' in request.form and 'address' in request.form :
        fname = request.form['fname']
        lname = request.form['lname']
        address = request.form['address']
        username = request.form['username']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        print(fname,lname,address,username,phone,email,password)
        cursor =  mysql.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute("INSERT INTO accounts (fname,lname,address,username,phone,email,pass,usertype) VALUES (%s, %s,%s,%s, %s,%s,%s, %s)", (fname,lname,address,username,phone,email,password,"customer"))
            mysql.commit()
            msg = 'You have successfully registered !'
            return render_template('Custlogin.html', msg = msg)
        cursor.close()
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('Custregister.html', msg = msg)

@app.route('/agentregister', methods =['GET', 'POST'])
def agentregister():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'fname' in request.form  and 'lname' in request.form and 'email' in request.form and 'phone' in request.form and 'address' in request.form :
        fname = request.form['fname']
        lname = request.form['lname']
        address = request.form['address']
        username = request.form['username']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        print(fname,lname,address,username,phone,email,password)
        cursor =  mysql.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute("INSERT INTO accounts (fname,lname,address,username,phone,email,pass,usertype) VALUES (%s, %s,%s,%s, %s,%s,%s, %s)", (fname,lname,address,username,phone,email,password,"agent"))
            mysql.commit()
            msg = 'You have successfully registered !'
            return render_template('Agentlogin.html', msg = msg)
        cursor.close()
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('Agentregister.html', msg = msg)

@app.route('/agentlogin', methods =['GET', 'POST'])
def agentlogin():
    msg = ''
    print(request.method)
    print(request.form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND pass = %s', (username, password))
        account = cursor.fetchone()
        cursor.close()
        print(account,"Hello 123789")
        if account:
            if account[7] != 'agent':
                return render_template('Custlogin.html', alert="Please login as a Customer to access this page!")
            if username == account[3] and password == account[6]:
                msg = 'Logged in successfully !'
                return render_template('index.html', msg = msg)
            else:
                msg = 'Incorrect username / password !'
                return render_template('Agentlogin.html', msg = msg)
        else:
            return render_template('main.html',msg='Username or Password is incorrect!')
    
    

@app.route('/adminlogin', methods =['GET', 'POST'])
def adminlogin():
    msg = ''
    print(request.method)
    print(request.form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND pass = %s', (username, password))
        account = cursor.fetchone()
        cursor.close()
        print(account,"Hello 123789")
        if account:
            if account[7] != 'admin':
                return render_template('Custlogin.html', alert="Please login as a Customer to access this page!")
            if username == account[3] and password == account[6]:
                msg = 'Logged in successfully !'
                return render_template('index.html', msg = msg)
            else:
                msg = 'Incorrect username / password !'
                return render_template('main.html', msg = msg)
        else:
            return render_template('main.html',msg='Username or Password is incorrect!')
    

if __name__ == '__main__':
    app.run(debug=True)
