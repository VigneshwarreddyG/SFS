import unittest
from flask_testing import TestCase
from app import app

# Create a test class for the Flask application
class TestApp(TestCase):
    # Method to create the Flask application with testing configurations
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    # Test case for the index route
    def test_index_route(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('main.html')

    # Test case for the customer registration route
    def test_customer_register_route(self):
        response = self.client.get('/Custregisterhtml')
        self.assert200(response)
        self.assert_template_used('Custregister.html')

    # Test case for the customer login route
    def test_customer_login_route(self):
        response = self.client.get('/Custloginhtml')
        self.assert200(response)
        self.assert_template_used('Custlogin.html')

    # Test case for the agent login route
    def test_agent_login_route(self):
        response = self.client.get('/Agentloginhtml')
        self.assert200(response)
        self.assert_template_used('agentlogin.html')

    # Test case for the agent registration route
    def test_agent_register_route(self):
        response = self.client.get('/Ageregisterhtml')
        self.assert200(response)
        self.assert_template_used('Agentregister.html')

    # Test case for the admin login route
    def test_admin_login_route(self):
        response = self.client.get('/Admin')
        self.assert200(response)
        self.assert_template_used('Adminlogin.html')

    # Test case for the agent dashboard route
    def test_agent_dashboard_route(self):
        response = self.client.get('/agentdashboard')
        self.assert200(response)

    # Test case for the car booking route with form data
    def test_car_booking_route(self):
        response = self.client.post('/Carbooking', data={'carModel': 'TestModel', 'paymentInfo': 'TestPayment', 'modelNumber': 'TestModelNumber', 'appointmentDate': '2023-01-01'})
        print("::::::::::::::::::::::")
        print(response)
        self.assert200(response)
        # Add assertions for the behavior of the Carbooking route based on the form data

    # Test case for customer login with valid credentials
    def test_customer_login_valid_credentials(self):
        response = self.client.post('/customerlogin', data={'username': 'valid_username', 'password': 'valid_password'})
        self.assertStatus(response, 200)  # Check for a redirect status
        response = self.client.get(response.headers['Location'])  # Follow the redirect
        self.assert200(response)
        self.assert_template_used('CustomerDashboard.html')

    # Test case for customer login with valid credentials and additional assertions
    def test_customer_login_valid_credentials_with_assertions(self):
        response = self.client.post('/customerlogin', data={'username': 'valid_username', 'password': 'valid_password'})
        self.assertStatus(response, 302)  # Check for a redirect status
        response = self.client.get(response.headers['Location'])  # Follow the redirect
        self.assert200(response)
        # Add more assertions based on the expected behavior after a successful login
        self.assert_template_used('ExpectedTemplateAfterLogin.html')

    # Test case for customer registration with valid data
    def test_customer_register_valid_data(self):
        response = self.client.post('/customerregister', data={'fname': 'John', 'lname': 'Doe', 'address': '123 Main St', 'username': 'john_doe', 'phone': '1234567890', 'email': 'john.doe@example.com', 'password': 'secure_password'})
        self.assert200(response)
        self.assert_template_used('Custlogin.html')
        # Add more assertions based on the expected behavior when using valid registration data

    # Test case for customer registration with an existing username
    def test_customer_register_existing_username(self):
        # Ensure this username already exists in your database
        response = self.client.post('/customerregister', data={'fname': 'John', 'lname': 'Doe', 'address': '123 Main St', 'username': 'existing_username', 'phone': '1234567890', 'email': 'john.doe@example.com', 'password': 'secure_password'})
        self.assert200(response)
        self.assert_template_used('Custregister.html')

# Run the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
