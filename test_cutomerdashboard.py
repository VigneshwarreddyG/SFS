import pytest
from flask import Flask
from app import app  # Import your Flask app

# Define a Pytest fixture to create a test client
@pytest.fixture
def client():
    client = app.test_client()
    return client

# Test case to check the response status code for the admin dashboard route
def test_admin_dashboard_response(client):
    response = client.get('/customer_dashboard')
    print('hello')  # Print a message for debugging or verification
    assert response.status_code == 200  # Assert that the response status code is 200

# Test case to check the content of the admin dashboard route
def test_admin_dashboard_content(client):
    response = client.get('/customer_dashboard')
    content = response.get_data(as_text=True)  # Get the response content as text
    assert "Welcome to the Customer Dashboard" in content  # Assert that a specific content is present in the response
