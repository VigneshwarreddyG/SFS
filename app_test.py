import unittest
from app import app, mysql  # Import your Flask app and MySQL connection
from flask import request
import app  # Import your Flask app module

class AdminLoginTestCase(unittest.TestCase):

    def setUp(self):
        # Set up a test client and a testing environment
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        # Clean up after the test
        pass

    def test_successful_login(self):
        # Test a successful login
        response = self.app.post('/adminlogin', data=dict(username='admin_user', password='admin_pass'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logged in successfully', response.data)

    def test_invalid_credentials(self):
        # Test login with invalid credentials
        response = self.app.post('/adminlogin', data=dict(username='invalid_user', password='invalid_pass'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Incorrect username / password', response.data)

    def test_account_type_check(self):
        # Test login with a non-admin account
        response = self.app.post('/adminlogin', data=dict(username='non_admin_user', password='non_admin_pass'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please login as a Customer', response.data)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
