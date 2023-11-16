import unittest
from flask_testing import TestCase
from app import app,mysql
class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['MYSQL_DATABASE'] = 'SFS'
        return app

    def test_index_route(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('main.html')

    def test_customer_register_route(self):
        response = self.client.get('/Custregisterhtml')
        self.assert200(response)
        self.assert_template_used('Custregister.html')

    def test_customer_login_route(self):
        response = self.client.get('/Custloginhtml')
        self.assert200(response)
        self.assert_template_used('Custlogin.html')

    def test_agent_register_route(self):
        response = self.client.get('/Ageregisterhtml')
        self.assert200(response)
        self.assert_template_used('Agentregister.html')

    def test_admin_login_route(self):
        response = self.client.get('/Admin')
        self.assert200(response)
        self.assert_template_used('Adminlogin.html')
    
    def test_customer_login_valid_credentials(self):
        response = self.client.post('/customerlogin', data={'username': 'admin', 'password': 'admin'})
        self.assertStatus(response, 200)  

    def test_customer_register_valid_data(self):
        response = self.client.post('/customerregister', data={'fname': 'John', 'lname': 'Doe', 'address': '123 Main St', 'username': 'john_doe', 'phone': '1234567890', 'email': 'john.doe@example.com', 'password': 'secure_password'})
        self.assert200(response)
        self.assert_template_used('Custlogin.html')


    def setUp(self):
        self.app = self.create_app()
        self.client = self.app.test_client()
        with self.app.app_context():
            # Create tables in the test database
            cursor = mysql.cursor()
            # Add your table creation queries here
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS accounts (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    fname VARCHAR(255),
                    lname VARCHAR(255),
                    address VARCHAR(255),
                    username VARCHAR(255) UNIQUE,
                    phone VARCHAR(20),
                    email VARCHAR(255),
                    pass VARCHAR(255),
                    usertype VARCHAR(255)
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS accomodationservice (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nameofcustomer VARCHAR(255),
                    ApartmentDetails VARCHAR(255),
                    members INT,
                    location VARCHAR(255),
                    movein DATE
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS groceries (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    Nameofcustomer VARCHAR(255),
                    item VARCHAR(255),
                    quantity INT,
                    pickupTime DATETIME,
                    dropTime DATETIME
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS car_service (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nameofcustomer VARCHAR(255),
                    carModel VARCHAR(255),
                    paymentInfo VARCHAR(255),
                    modelNumber VARCHAR(255),
                    appointmentDate DATE,
                    pickupTime DATETIME,
                    dropTime DATETIME
                )
            """)
            mysql.commit()
            cursor.close()

    def tearDown(self):
        with self.app.app_context():
            # Drop tables in the test database
            cursor = mysql.cursor()
            # Add your table dropping queries here
            cursor.execute("DROP TABLE IF EXISTS accounts")
            cursor.execute("DROP TABLE IF EXISTS accomodationservice")
            cursor.execute("DROP TABLE IF EXISTS groceries")
            cursor.execute("DROP TABLE IF EXISTS car_service")
            mysql.commit()
            cursor.close()

    def test_database_operations(self):
        # Test your database operations here
        with self.app.app_context():
            # Example: Insert data into the accounts table
            cursor = mysql.cursor()
            cursor.execute("""
                INSERT INTO accounts (fname, lname, address, username, phone, email, pass, usertype)
                VALUES ('John', 'Doe', '123 Main St', 'john_doe', '1234567890', 'john.doe@example.com', 'secure_password', 'customer')
            """)
            mysql.commit()

            # Check if the data is present in the table
            cursor.execute("SELECT * FROM accounts WHERE username = 'john_doe'")
            account = cursor.fetchone()
            cursor.close()
            self.assertIsNotNone(account)
            self.assertEqual(account[1], 'John')
            self.assertEqual(account[2], 'Doe')

if __name__ == '_main_':
    unittest.main()