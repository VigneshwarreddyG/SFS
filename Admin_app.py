# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import re

# Create a Flask web application
app = Flask(__name__)

# MySQL configuration
# Establish a connection to the MySQL database
mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vigneshwar@94",
    database="SFS"
)

# Define the route for the home page
@app.route('/')
def index():
    # Fetch user data from the database for customers
    cur = mysql.cursor()
    cur.execute("SELECT * FROM Accounts WHERE usertype = 'customer'")
    customers = cur.fetchall()
    print(customers)

    # Fetch user data from the database for agents
    cur.execute("SELECT * FROM Accounts WHERE usertype = 'agent'")
    agents = cur.fetchall()
    print(agents)

    cur.close()

    # Render the home page with user data
    return render_template('AdminDashboard copy.html', customers=customers, agents=agents)

# Define the route for editing a user
@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    cur = mysql.cursor()

    # Handle POST request to update user information
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Update user information in the database
        cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
        mysql.commit()

        # Redirect to the home page after updating
        return redirect(url_for('index'))

    # Fetch user information for the specified user_id
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()

    # Render the page for editing user information
    return render_template('edit_user.html', user=user)

# Define the route for deleting a user
@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    cur = mysql.cursor()

    # Delete the user from the database
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.commit()
    cur.close()

    # Redirect to the home page after deletion
    return redirect(url_for('index'))

# Run the Flask application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
