import pytest
from app import app
@pytest.fixture
#creating the client object with the flask
def client():
    client = app.test_client()
    return client

def test_admin_dashboard_response(client):
    response = client.get('/admin_dashboard')
    assert response.status_code == 200
# Testing the admin dash board containing the content in it
def test_admin_dashboard_content(client):
    response = client.get('/admin_dashboard')
    content = response.get_data(as_text=True)
    assert "Welcome to the Admin Dashboard" in content


