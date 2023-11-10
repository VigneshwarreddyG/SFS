import pytest
from flask import Flask
from app import app  # Import your Flask app

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_admin_dashboard_response(client):
    response = client.get('/customer_dashboard')
    print('hello')
    assert response.status_code == 200
# Testing the admin dash board containing the content in it
def test_admin_dashboard_content(client):
    response = client.get('/customer_dashboard')
    content = response.get_data(as_text=True)
    assert "Welcome to the Customer Dashboard" in content
    