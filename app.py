from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import re

app = Flask(__name__)

# MySQL configuration
mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Saicharan@27",
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

@app.route('/logout', methods=['GET'])
def logout():
    return redirect(url_for('index'))



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
            # if account[3] == 'admin':
            #      return render_template('Custlogin.html', alert="Please login as a Customer to access this page!")
            if username == account[3] and password == account[6]:
                msg = 'Logged in successfully !'
                return render_template('CustomerDashboard.html', msg = msg)
            else:
                msg = 'Incorrect username / password !'
                return render_template('Custlogin.html', msg = msg)
        else:
            return render_template('main.html',msg='Username or Password is incorrect!')

@app.route('/groceryservice', methods =['GET', 'POST'])
def groceryservice():
    return render_template('groceryservice.html')

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
                return render_template('AgentDashboard.html')
            if username == account[3] and password == account[6]:
                msg = 'Logged in successfully !'
                return render_template('AgentDashboard.html', msg = msg)
            else:
                msg = 'Incorrect username / password !'
                return render_template('Agentlogin.html', msg = msg)
        else:
            return render_template('main.html',msg='Username or Password is incorrect!')
    
@app.route('/Carbooking')
def Carbooking():
    return render_template('Carbooking.html')

@app.route('/Accomodationservice')
def Accomodationservice():
    return render_template('Accomodationservice.html')

@app.route('/Accomodationlist')
def Accomodationlist():
        cursor = mysql.cursor()
        cursor.execute("SELECT nameofcustomer, ApartmentDetails, members, location,movein FROM accomodationservices")
        booking_data = cursor.fetchall()
        print(booking_data)
        cursor.close()
        return render_template('Accomdationlist.html',data=booking_data)

@app.route('/Accomodationserviceform', methods=['POST'])
def Accomodationserviceform():
    if request.method == 'POST':
        nameofcustomer = request.form['nameofcustomer']
        ApartmentDetails = request.form['ApartmentDetails']
        members = request.form['members']
        location = request.form['location']
        movein = request.form['movein']
        insert_query = "INSERT INTO accomodationservices (nameofcustomer, ApartmentDetails, members, location, movein) VALUES (%s, %s, %s, %s, %s)"
        values = (nameofcustomer, ApartmentDetails, members, location, movein)
        cursor = mysql.cursor()
        cursor.execute(insert_query, values)
        mysql.commit()
        return redirect(url_for('customer_dashboard'))
        
@app.route('/Groceryserviceform', methods=['POST'])
def Groceryserviceform():
    if request.method == 'POST':
        nameofcustomer = request.form['nameofcustomer']
        items = request.form.getlist('items[]')
        quantities = request.form.getlist('quantities[]')
        pickupTime = request.form['pickupTime']
        dropTime=request.form['dropTime']
        cursor = mysql.cursor()
        for item, quantity in zip(items, quantities):
            cursor.execute("INSERT INTO grocery (Nameofcustomer,item, quantity,pickupTime,dropTime) VALUES (%s, %s,%s,%s,%s)", (nameofcustomer,item, quantity,pickupTime,dropTime))
        mysql.commit()
        cursor.close()
    return redirect(url_for('customer_dashboard'))


@app.route('/Carserviceform', methods=['POST'])
def Carserviceform():
    if request.method == 'POST':
        nameofcustomer = request.form['nameofcustomer']
        carModel = request.form['carModel']
        paymentInfo = request.form['paymentInfo']
        modelNumber = request.form['modelNumber']
        appointmentDate = request.form['appointmentDate']
        pickupTime = request.form['pickupTime']
        dropTime=request.form['dropTime']
        # Insert the form data into the MySQL database
        query = "INSERT INTO car_service (nameofcustomer,carModel, paymentInfo, modelNumber, appointmentDate,pickupTime,dropTime) VALUES (%s,%s, %s, %s, %s,%s,%s)"
        values = (nameofcustomer,carModel, paymentInfo, modelNumber, appointmentDate,pickupTime,dropTime)
        cursor = mysql.cursor()
        cursor.execute(query, values)
        mysql.commit()
        return redirect(url_for('customer_dashboard'))
    
@app.route('/customer_dashboard')
def customer_dashboard():
    return render_template('CustomerDashboard.html')


@app.route('/Carbookinglist')
def Carbookinglist():
        cursor = mysql.cursor()
        cursor.execute("SELECT carModel, paymentInfo, modelNumber, appointmentDate,pickupTime,dropTime,nameofcustomer FROM car_service")
        booking_data = cursor.fetchall()
        print(booking_data)
        cursor.close()
        return render_template('Carbookinglist.html',data=booking_data)

@app.route('/grocerylist')
def grocerylist():
        cursor = mysql.cursor()
        cursor.execute("SELECT Nameofcustomer,item, quantity,pickupTime,dropTime FROM grocery")
        booking_data = cursor.fetchall()
        print(booking_data)
        cursor.close()
        return render_template('groceryplans.html',data=booking_data)

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
                return render_template('CustomerDashboard.html', msg = msg)
            else:
                msg = 'Incorrect username / password !'
                return render_template('main.html', msg = msg)
        else:
            return render_template('main.html',msg='Username or Password is incorrect!')
    

if __name__ == '__main__':
    app.run(debug=True)
# print("Write you secret message here")
