# Importing  necessary modules from Flask and MySQL connector
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import re

# Initializing the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'saaa'

# Connect to the MySQL database
mysql = mysql.connector.connect(
    host="mysql-container",
    user="root",
    password="Saicharan@27",
    database="SFS"
)

# Defining the route for the main page
@app.route('/', methods=['POST', 'GET'])
def index():
    # Fetch all user records from the 'accounts' table
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM accounts")
    users = cursor.fetchall()
    cursor.close()
    return render_template('main.html', users=users)

# Defining the route for the admin dashboard
@app.route('/admin_index')
def admin_index():
    # Fetch customer and agent records from the 'accounts' table
    cur = mysql.cursor()
    cur.execute("SELECT * FROM Accounts WHERE usertype = 'customer'")
    customers = cur.fetchall()
    cur.execute("SELECT * FROM Accounts WHERE usertype = 'agent'")
    agents = cur.fetchall()
    cur.close()
    return render_template('admindashboard.html', customers=customers, agents=agents)

# Defining the route for the customer registration form
@app.route('/Custregisterhtml', methods=['POST', 'GET'])
def Custregisterhtml():
    return render_template('Custregister.html')

# Define the route for the logout functionality
@app.route('/logout', methods=['GET'])
def logout():
    return redirect(url_for('index'))

# Define the route for the customer login form
@app.route('/Custloginhtml', methods=['POST', 'GET'])
def Custloginhtml():
    return render_template('Custlogin.html')

# Define the route for the agent login form
@app.route('/Ageloginhtml', methods=['POST', 'GET'])
def Agentloginhtml():
    return render_template('Agentlogin.html')

# Define the route for the agent registration form
@app.route('/Ageregisterhtml', methods=['POST', 'GET'])
def Ageregisterhtml():
    return render_template('Agentregister.html')

# Define the route for the admin login form
@app.route('/Admin', methods=['POST', 'GET'])
def Adminlogin():
    return render_template('Adminlogin.html')

# Define the route for customer login
@app.route('/customerlogin', methods=['GET', 'POST'])
def customerlogin():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Fetch user account from the 'accounts' table based on username and password
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.cursor()
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND pass = %s', (username, password))
        account = cursor.fetchone()
        cursor.close()
        print(account, "Hello 123789")
        if account:
            if username == account[3] and password == account[6]:
                # Successful login, store username in the session
                msg = 'Logged in successfully!'
                session['username'] = username
                print(session['username'])  # Debugging statement
                print("username after logging in")
                
                # Redirect to the customer dashboard
                return render_template('dashboardcustomer.html', username=username, msg=msg)
            else:
                msg = 'Incorrect username / password!'
                return render_template('Custlogin.html', msg=msg)
        else:
            # Redirect to the main page with an error message
            return render_template('main.html', msg='Username or Password is incorrect!')

# Define the route for the grocery service
@app.route('/groceryservice', methods=['GET', 'POST'])
def groceryservice():
    grocery = ""
    return render_template('groceryservice.html', grocery=grocery)

# Define the route for the customer grocery service
@app.route('/customergroceryservice', methods=['GET', 'POST'])
def customergroceryservice():
    grocery = ""
    return render_template('customergroceryservice.html', grocery=grocery)

# Define the route for customer registration
@app.route('/customerregister', methods=['GET', 'POST'])
def customerregister():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'fname' in request.form and 'lname' in request.form and 'email' in request.form and 'phone' in request.form and 'address' in request.form:
        # Fetch registration form data
        fname = request.form['fname']
        lname = request.form['lname']
        address = request.form['address']
        username = request.form['username']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']
        print(fname, lname, address, username, phone, email, password)
        cursor = mysql.cursor()
        # Check if the username already exists
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        print(account)
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Insert new account data into the 'accounts' table
            cursor.execute(
                "INSERT INTO accounts (fname,lname,address,username,phone,email,pass,usertype) VALUES (%s, %s,%s,%s, %s,%s,%s, %s)",
                (fname, lname, address, username, phone, email, password, "customer"))
            mysql.commit()
            msg = 'You have successfully registered !'
            # Redirect to the customer login page with a success message
            return render_template('Custlogin.html', msg=msg)
        cursor.close()
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    # Render the customer registration page with appropriate messages
    return render_template('Custregister.html', msg=msg)


@app.route('/delete_accomodation/<int:id>')
def delete_accomodation(id):
    cursor = mysql.cursor()
    # Fetch the details of the accommodation before deleting (optional, for confirmation message)
    cursor.execute("SELECT * FROM accomodationservices WHERE id = %s", (id,))
    accommodation = cursor.fetchone()
    # Delete the accommodation based on the provided id
    cursor.execute("DELETE FROM accomodationservices WHERE id = %s", (id,))
    mysql.commit()
    cursor.close()
    # Optionally, you can provide a confirmation message or redirect to a different page
    # In this example, redirecting to the Accomodationlist route
    return redirect(url_for('Accomodationlist'))

@app.route('/editcarbooking/<int:id>', methods=['GET', 'POST'])
def editcarbooking(id):
    cursor = mysql.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM carservices WHERE id = %s", (id,))
        carbooking = cursor.fetchone()
        cursor.close()
        print("::::::::::::::::::::::::::::::::::")
        print("carbooking",carbooking[0])
        print("carbooking",carbooking[2])
        print("carbooking",carbooking[6])
        print("carbooking",carbooking[7])
        return render_template('carbooking.html', carbooking=carbooking)
    elif request.method == 'POST':
        # Fetch the existing car booking details
        cursor.execute("SELECT * FROM carservices WHERE id = %s", (id,))
        existing_carbooking = cursor.fetchone()

        # Update only the fields that have changed
        update_query = """
            UPDATE carservices
            SET car_model=%s, payment_info=%s, model_number=%s, appointment_date=%s, pickup_time=%s, drop_time=%s
            WHERE id = %s
        """
        update_values = (
            request.form['carModel'] if request.form['carModel'] is not None else existing_carbooking[1],
            request.form['paymentInfo'] if request.form['paymentInfo'] is not None else existing_carbooking[2],
            request.form['modelNumber'] if request.form['modelNumber'] is not None else existing_carbooking[3],
            request.form['appointmentDate'] if request.form['appointmentDate'] is not None else existing_carbooking[4],
            request.form['pickupTime'] if request.form['pickupTime'] is not None else existing_carbooking[5],
            request.form['dropTime'] if request.form['dropTime'] is not None else existing_carbooking[6],
            id
        )

        cursor.execute(update_query, update_values)
        mysql.commit()
        cursor.close()
        print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        return redirect(url_for('Carbooking'))

@app.route('/deletecarbooking/<int:id>')
def deletecarbooking(id):
    cursor = mysql.cursor()

    # Fetch the details of the car booking before deleting (optional, for confirmation message)
    cursor.execute("SELECT * FROM carservices WHERE id = %s", (id,))
    car_booking = cursor.fetchone()
    # Delete the car booking based on the provided id
    cursor.execute("DELETE FROM carservices WHERE id = %s", (id,))
    mysql.commit()
    cursor.close()
    # Optionally, you can provide a confirmation message or redirect to a different page
    # In this example, redirecting to the car_service_list route
    return redirect(url_for('Carbookinglist'))




@app.route('/edit_accomodation/<int:id>', methods=['GET', 'POST'])
def edit_accomodation(id):
    cursor = mysql.cursor()
    if request.method == 'GET':
        cursor.execute("SELECT * FROM accomodationservices WHERE id = %s", (id,))
        accommodation = cursor.fetchone()
        cursor.close()
        return render_template('Accomodationservice.html', accommodation=accommodation)
    elif request.method == 'POST':
        # Update the accommodation details based on the provided id
        cursor.execute("""
            UPDATE accomodationservices
            SET nameofcustomer=%s, ApartmentDetails=%s, members=%s, location=%s, movein=%s
            WHERE id = %s
        """, (request.form['nameofcustomer'], request.form['ApartmentDetails'], request.form['members'], request.form['location'], request.form['movein'], id))

        mysql.commit()
        cursor.close()
        return redirect(url_for('Accomodationlist'))


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
    carbooking=""
    return render_template('Carbooking.html',carbooking=carbooking)
@app.route('/customerCarbooking')
def customerCarbooking():
    carbooking=""
    return render_template('customerCarbooking.html',carbooking=carbooking)

@app.route('/Accomodationservice')
def Accomodationservice():
    accommodation=""
    return render_template('Accomodationservice.html',accommodation=accommodation)

@app.route('/customerAccomodationservice')
def customerAccomodationservice():
    accommodation=""
    return render_template('customerAccomodationservice.html',accommodation=accommodation)


@app.route('/Accomodationlist')
def Accomodationlist():
        cursor = mysql.cursor()
        cursor.execute("SELECT nameofcustomer, ApartmentDetails, members, location,movein,id FROM accomodationservices")
        booking_data = cursor.fetchall()
        print(booking_data)
        cursor.close()
        return render_template('Accomdationlist.html',data=booking_data)
@app.route('/customeraccomodationlist')
def customeraccomodationlist():
        username = session.get('username')
        cursor = mysql.cursor()
        cursor.execute("SELECT nameofcustomer, ApartmentDetails, members, location,movein,id FROM accomodationservices  WHERE nameofcustomer = %s", (username,))
        booking_data = cursor.fetchall()
        print(booking_data)
        cursor.close()
        return render_template('customeraccomodationlist.html',data=booking_data)

# Add the following route to handle the form submission
@app.route('/customeraccomodationlist', methods=['POST'])
def handle_customer_accomodation_list():
    # Process the form data here if needed
    # ...

    # Redirect to the 'customeraccomodationlist' route after processing the form
    return redirect(url_for('customeraccomodationlist'))

@app.route('/Accomodationserviceform', methods=['POST'])
def Accomodationserviceform():
    if request.method == 'POST':
        # Get the form data
        nameofcustomer = request.form['nameofcustomer']
        ApartmentDetails = request.form['ApartmentDetails']
        members = request.form['members']
        location = request.form['location']
        movein = request.form['movein']
        submitted_id = request.form.get('id')  # Assuming you have an input with name 'id' in your form

        # Check if the submitted ID exists
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM accomodationservices WHERE id = %s", (submitted_id,))
        existing_record = cursor.fetchone()
        cursor.close()

        if existing_record:
            # If the ID exists, update the existing record
            update_query = """
                UPDATE accomodationservices
                SET nameofcustomer=%s, ApartmentDetails=%s, members=%s, location=%s, movein=%s
                WHERE id = %s
            """
            update_values = (
                nameofcustomer, ApartmentDetails, members, location, movein, submitted_id
            )

            cursor = mysql.cursor()
            cursor.execute(update_query, update_values)
            mysql.commit()
            cursor.close()
        else:
            # If the ID doesn't exist, insert a new record
            insert_query = """
                INSERT INTO accomodationservices (nameofcustomer, ApartmentDetails, members, location, movein)
                VALUES (%s, %s, %s, %s, %s)
            """
            insert_values = (
                nameofcustomer, ApartmentDetails, members, location, movein
            )

            cursor = mysql.cursor()
            cursor.execute(insert_query, insert_values)
            mysql.commit()
            cursor.close()
        return redirect(url_for('customer_dashboard'))

@app.route('/customerAccomodationserviceform', methods=['POST'])
def customerAccomodationserviceform():
    if request.method == 'POST':
        # Get the form data
        nameofcustomer = request.form['nameofcustomer']
        ApartmentDetails = request.form['ApartmentDetails']
        members = request.form['members']
        location = request.form['location']
        movein = request.form['movein']
        submitted_id = request.form.get('id')  # Assuming you have an input with name 'id' in your form

        # Check if the submitted ID exists
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM accomodationservices WHERE id = %s", (submitted_id,))
        existing_record = cursor.fetchone()
        cursor.close()

        if existing_record:
            # If the ID exists, update the existing record
            update_query = """
                UPDATE accomodationservices
                SET nameofcustomer=%s, ApartmentDetails=%s, members=%s, location=%s, movein=%s
                WHERE id = %s
            """
            update_values = (
                nameofcustomer, ApartmentDetails, members, location, movein, submitted_id
            )

            cursor = mysql.cursor()
            cursor.execute(update_query, update_values)
            mysql.commit()
            cursor.close()
        else:
            # If the ID doesn't exist, insert a new record
            insert_query = """
                INSERT INTO accomodationservices (nameofcustomer, ApartmentDetails, members, location, movein)
                VALUES (%s, %s, %s, %s, %s)
            """
            insert_values = (
                nameofcustomer, ApartmentDetails, members, location, movein
            )

            cursor = mysql.cursor()
            cursor.execute(insert_query, insert_values)
            mysql.commit()
            cursor.close()
        return redirect(url_for('dashboardcustomer'))

        
@app.route('/Groceryserviceform', methods=['POST'])
def Groceryserviceform():
    if request.method == 'POST':
        # Get the form data
        nameofcustomer = request.form['nameofcustomer']
        items = request.form.getlist('items[]')
        quantities = request.form.getlist('quantities[]')
        pickupTime = request.form['pickupTime']
        dropTime = request.form['dropTime']
        submitted_id = request.form.get('id')  # Assuming you have an input with name 'id' in your form

        # Check if the submitted ID exists
        if submitted_id:
            cursor = mysql.cursor()
            cursor.execute("SELECT * FROM grocery WHERE id = %s", (submitted_id,))
            existing_record = cursor.fetchone()
            cursor.close()

            if existing_record:
                # If the ID exists, update the existing record
                cursor = mysql.cursor()
                cursor.execute("UPDATE grocery SET Nameofcustomer = %s, item = %s, quantity = %s, pickupTime = %s, dropTime = %s WHERE id = %s",
                               (nameofcustomer, items[0], quantities[0], pickupTime, dropTime, submitted_id))
                mysql.commit()
                cursor.close()
                return redirect(url_for('customer_dashboard'))

        # If no ID or ID does not exist, insert a new record
        cursor = mysql.cursor()
        for item, quantity in zip(items, quantities):
            cursor.execute("INSERT INTO grocery (Nameofcustomer, item, quantity, pickupTime, dropTime) VALUES (%s, %s, %s, %s, %s)",
                           (nameofcustomer, item, quantity, pickupTime, dropTime))
        mysql.commit()
        cursor.close()

        return redirect(url_for('customer_dashboard'))

@app.route('/customerGroceryserviceform', methods=['POST'])
def customerGroceryserviceform():
    if request.method == 'POST':
        # Get the form data
        nameofcustomer = request.form['nameofcustomer']
        items = request.form.getlist('items[]')
        quantities = request.form.getlist('quantities[]')
        pickupTime = request.form['pickupTime']
        dropTime = request.form['dropTime']
        submitted_id = request.form.get('id')  # Assuming you have an input with name 'id' in your form

        # Check if the submitted ID exists
        if submitted_id:
            cursor = mysql.cursor()
            cursor.execute("SELECT * FROM grocery WHERE id = %s", (submitted_id,))
            existing_record = cursor.fetchone()
            cursor.close()

            if existing_record:
                # If the ID exists, update the existing record
                cursor = mysql.cursor()
                cursor.execute("UPDATE grocery SET Nameofcustomer = %s, item = %s, quantity = %s, pickupTime = %s, dropTime = %s WHERE id = %s",
                               (nameofcustomer, items[0], quantities[0], pickupTime, dropTime, submitted_id))
                mysql.commit()
                cursor.close()
                return redirect(url_for('dashboardcustomer'))

        # If no ID or ID does not exist, insert a new record
        cursor = mysql.cursor()
        for item, quantity in zip(items, quantities):
            cursor.execute("INSERT INTO grocery (Nameofcustomer, item, quantity, pickupTime, dropTime) VALUES (%s, %s, %s, %s, %s)",
                           (nameofcustomer, item, quantity, pickupTime, dropTime))
        mysql.commit()
        cursor.close()

        return redirect(url_for('dashboardcustomer'))



@app.route('/Carserviceform', methods=['POST'])
def Carserviceform():
    if request.method == 'POST':
        # Get the form data
        nameofcustomer = request.form['nameofcustomer']
        carModel = request.form['carModel']
        paymentInfo = request.form['paymentInfo']
        modelNumber = request.form['modelNumber']
        appointmentDate = request.form['appointmentDate']
        pickupTime = request.form['pickupTime']
        dropTime = request.form['dropTime']
        submitted_id = request.form.get('id')  # Assuming you have an input with name 'id' in your form

        # Check if the submitted ID exists
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM carservices WHERE id = %s", (submitted_id,))
        existing_record = cursor.fetchone()
        cursor.close()

        if existing_record:
            # If the ID exists, update the existing record
            update_query = """
                UPDATE carservices
                SET nameofcustomer=%s, carModel=%s, paymentInfo=%s, modelNumber=%s,
                    appointmentDate=%s, pickupTime=%s, dropTime=%s
                WHERE id = %s
            """
            update_values = (
                nameofcustomer, carModel, paymentInfo, modelNumber,
                appointmentDate, pickupTime, dropTime, submitted_id
            )

            cursor = mysql.cursor()
            cursor.execute(update_query, update_values)
            mysql.commit()
            cursor.close()
        else:
            # If the ID doesn't exist, insert a new record
            insert_query = """
                INSERT INTO carservices (nameofcustomer, carModel, paymentInfo, modelNumber,
                                        appointmentDate, pickupTime, dropTime)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            insert_values = (
                nameofcustomer, carModel, paymentInfo, modelNumber,
                appointmentDate, pickupTime, dropTime
            )
            cursor = mysql.cursor()
            cursor.execute(insert_query, insert_values)
            mysql.commit()
            cursor.close()

        return redirect(url_for('customer_dashboard'))

@app.route('/customerCarserviceform', methods=['POST'])
def customerCarserviceform():
    if request.method == 'POST':
        # Get the form data
        nameofcustomer = request.form['nameofcustomer']
        carModel = request.form['carModel']
        paymentInfo = request.form['paymentInfo']
        modelNumber = request.form['modelNumber']
        appointmentDate = request.form['appointmentDate']
        pickupTime = request.form['pickupTime']
        dropTime = request.form['dropTime']
        submitted_id = request.form.get('id')  # Assuming you have an input with name 'id' in your form

        # Check if the submitted ID exists
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM carservices WHERE id = %s", (submitted_id,))
        existing_record = cursor.fetchone()
        cursor.close()

        if existing_record:
            # If the ID exists, update the existing record
            update_query = """
                UPDATE carservices
                SET nameofcustomer=%s, carModel=%s, paymentInfo=%s, modelNumber=%s,
                    appointmentDate=%s, pickupTime=%s, dropTime=%s
                WHERE id = %s
            """
            update_values = (
                nameofcustomer, carModel, paymentInfo, modelNumber,
                appointmentDate, pickupTime, dropTime, submitted_id
            )

            cursor = mysql.cursor()
            cursor.execute(update_query, update_values)
            mysql.commit()
            cursor.close()
        else:
            # If the ID doesn't exist, insert a new record
            insert_query = """
                INSERT INTO carservices (nameofcustomer, carModel, paymentInfo, modelNumber,
                                        appointmentDate, pickupTime, dropTime)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            insert_values = (
                nameofcustomer, carModel, paymentInfo, modelNumber,
                appointmentDate, pickupTime, dropTime
            )
            cursor = mysql.cursor()
            cursor.execute(insert_query, insert_values)
            mysql.commit()
            cursor.close()

        return redirect(url_for('dashboardcustomer'))

    
@app.route('/customer_dashboard')
def customer_dashboard():
    
    username = session.get('username')
    return render_template('CustomerDashboard.html',username=username)


@app.route('/dashboardcustomer',methods=['POST','GET'])
def dashboardcustomer():
    username = session.get('username')
    return render_template('dashboardcustomer.html',username=username)

@app.route('/Carbookinglist')
def Carbookinglist():
        cursor = mysql.cursor()
        cursor.execute("SELECT carModel, paymentInfo, modelNumber, appointmentDate,pickupTime,dropTime,nameofcustomer,id FROM carservices")
        booking_data = cursor.fetchall()
        print(booking_data)
        cursor.close()
        return render_template('Carbookinglist.html',data=booking_data)

@app.route('/customercarlist')
def customercarlist():
        username = session.get('username')
        cursor = mysql.cursor()
        cursor.execute("SELECT carModel, paymentInfo, modelNumber, appointmentDate,pickupTime,dropTime,nameofcustomer,id FROM carservices  WHERE nameofcustomer = %s", (username,))
        booking_data = cursor.fetchall()
        print(booking_data)
        cursor.close()
        return render_template('customercarlist.html',data=booking_data)

@app.route('/grocerylist')
def grocerylist():
        cursor = mysql.cursor()
        cursor.execute("SELECT Nameofcustomer,item, quantity,pickupTime,dropTime,id FROM grocery")
        booking_data = cursor.fetchall()
        print(booking_data)
        cursor.close()
        return render_template('groceryplans.html',data=booking_data)

@app.route('/customergrocerylist')
def customergrocerylist():
        username = session.get('username')

        cursor = mysql.cursor()
        cursor.execute("SELECT Nameofcustomer,item, quantity,pickupTime,dropTime,id FROM grocery WHERE Nameofcustomer = %s", (username,))
        booking_data = cursor.fetchall()
        print(booking_data)
        cursor.close()
        return render_template('customergrocerylist.html',data=booking_data)


# Edit Grocery Service Booking
@app.route('/editgrocery/<int:id>', methods=['GET', 'POST'])
def editgrocery(id):
    cursor = mysql.cursor()
    if request.method == 'GET':
        # Fetch the details of the grocery service booking based on the provided ID
        cursor.execute("SELECT * FROM grocery WHERE id = %s", (id,))
        grocery = cursor.fetchone()
        cursor.close()
        print("grocery",grocery[3])
        
        return render_template('groceryservice.html', grocery=grocery)
    
    elif request.method == 'POST':
        # Update the grocery service booking based on the provided ID
        cursor.execute("""UPDATE grocery
            SET Nameofcustomer=%s, item=%s, quantity=%s, pickupTime=%s, dropTime=%s WHERE id = %s""", (request.form['nameofcustomer'], request.form['item'], request.form['quantity'], request.form['pickupTime'], request.form['dropTime'], id))
        mysql.commit()
        cursor.close()
        return redirect(url_for('groceryplans'))


# Delete Grocery Service Booking
@app.route('/deletegrocery/<int:id>')
def deletegrocery(id):
    cursor = mysql.cursor()
    # Fetch the details of the grocery service booking before deleting (optional, for confirmation message)
    cursor.execute("SELECT * FROM grocery WHERE id = %s", (id,))
    grocery_booking = cursor.fetchone()
    # Delete the grocery service booking based on the provided ID
    cursor.execute("DELETE FROM grocery WHERE id = %s", (id,))
    mysql.commit()
    cursor.close()
    # Optionally, you can provide a confirmation message or redirect to a different page
    # In this example, redirecting to the grocerylist route
    return redirect(url_for('grocerylist'))


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
        if username=='admin' and password=='admin' :
                msg = 'Logged in successfully !'
                cur = mysql.cursor()
                cur.execute("SELECT * FROM accounts WHERE usertype = 'customer'")
                customers = cur.fetchall()
                print(customers)
                cur.execute("SELECT * FROM accounts WHERE usertype = 'agent'")
                agents = cur.fetchall()
                print(agents)
                cur.close()
                return render_template('Admindashboard.html', customers=customers, agents=agents)
            
        
@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'POST':
        # Retrieve form data for editing the user
        fname = request.form['fname']
        email = request.form['email']
        # Update the user information in the database
        cursor = mysql.cursor()
        cursor.execute("UPDATE accounts SET fname = %s, email = %s WHERE phone = %s", (fname, email, str(user_id)))
        mysql.commit()
        cursor.close()
        # Redirect to the Admin Dashboard or any other desired page after editing
        return redirect(url_for('Admindashboard'))

    # Fetch user details from the database based on user_id
    cursor = mysql.cursor()
    cursor.execute("SELECT * FROM accounts WHERE phone = %s", (str(user_id),))

    user = cursor.fetchone()
    cursor.close()

    # Render the template for editing the user with the fetched details
    return render_template('edit_user.html', user=user)


# Flask route for deleting a user
@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    # Delete the user from the database based on user_id
    print(user_id,'hello1')
    cursor = mysql.cursor()
    cursor.execute("DELETE FROM accounts WHERE phone = %s", (str(user_id),))
    mysql.commit()
    cursor.close()
    
    # Redirect to the Admin Dashboard or any other desired page after deletion
    return redirect(url_for('admin_index'))

if __name__ == '__main__':
    app.run(debug=True)
# print("Write you secret message here")
