import pytest
from flask import Flask, url_for
from app import app  # Replace 'your_main_file_name' with the actual name of your main file

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_index_page(client):
    response = client.get('/')
    assert b'Welcome to the main page' in response.data
    assert response.status_code == 200

def test_customer_login(client):
    response = client.post('/customerlogin', data={'username': 'customer_username', 'password': 'customer_password'})
    assert b'Logged in successfully' in response.data
    assert response.status_code == 200

def test_agent_login(client):
    response = client.post('/agentlogin', data={'username': 'agent_username', 'password': 'agent_password'})
    assert b'Logged in successfully' in response.data
    assert response.status_code == 302  # Assuming a successful login redirects to another page

def test_invalid_login(client):
    response = client.post('/customerlogin', data={'username': 'invalid_username', 'password': 'invalid_password'})
    assert b'Incorrect username / password' in response.data
    assert response.status_code == 200

# Add more test cases as needed for other routes and functionalities

if __name__ == '__main__':
    pytest.main()

