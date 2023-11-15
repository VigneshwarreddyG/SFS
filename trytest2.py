import unittest
from unittest.mock import MagicMock, patch
from app import app, customerlogin  # Replace 'your_module' with your actual module name

class TestCustomerLogin(unittest.TestCase):
    def setUp(self):
        # Create a test client and application context
        self.app_context = app.app_context()
        self.app_context.push()
        self.app = app.test_client()

    def tearDown(self):
        # Clean up after each test
        self.app_context.pop()

    def test_valid_login(self):
        # Mocking the request object
        with self.app.test_request_context():
            mock_request = MagicMock()
            mock_request.method = 'POST'
            mock_request.form = {'username': 'vigneshwar', 'password': 'vigneshwar'}

            # Mocking the cursor and its execute and fetchone methods
            mock_cursor = MagicMock()
            mock_cursor.fetchone.return_value = ('vigneshwar', 'reddy', 'hyderabad', 'vigneshwar', '1234567890', 'vigneshwar@gmail.com', 'vigneshwar', 'customer')

            # Mocking the MySQL cursor
            with patch('app.mysql.cursor', return_value=mock_cursor):
                result = customerlogin(mock_request)
                self.assertEqual(result, 'CustomerDashboard.html')

    # Other test cases...

if __name__ == '__main__':
    unittest.main()
