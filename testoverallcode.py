import unittest
from flask_testing import TestCase
from app import app

class TestAppRoutes(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app


    def test_cust_register_html_route(self):
        response = self.client.get('/Custregisterhtml')
        self.assert200(response)
        self.assert_template_used('Custregister.html')

    def test_cust_login_html_route(self):
        response = self.client.get('/Custloginhtml')
        self.assert200(response)
        self.assert_template_used('Custlogin.html')

    def test_agent_login_html_route(self):
        response = self.client.get('/Ageloginhtml')
        self.assert200(response)
        self.assert_template_used('Agentlogin.html')

    def test_agent_register_html_route(self):
        response = self.client.get('/Ageregisterhtml')
        self.assert200(response)
        self.assert_template_used('Agentregister.html')

    def test_admin_login_route(self):
        response = self.client.get('/Admin')
        self.assert200(response)
        self.assert_template_used('Adminlogin.html')

if __name__ == '__main__':
    unittest.main()
