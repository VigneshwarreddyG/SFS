from flask import Flask, render_template, request, redirect, url_for,jsonify
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
@app.route('/')
def index():
    # Fetch user data from the database
    cur = mysql.cursor()
    cur.execute("SELECT * FROM Accounts WHERE usertype = 'customer'")
    customers = cur.fetchall()
    print(customers)
    cur.execute("SELECT * FROM Accounts WHERE usertype = 'agent'")
    agents = cur.fetchall()
    print(agents)
    cur.close()
    return render_template('AdminDashboard copy.html', customers=customers, agents=agents)

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    cur = mysql.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
        mysql.commit()

        return redirect(url_for('index'))

    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    return render_template('edit_user.html', user=user)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    cur = mysql.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.commit()
    cur.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
