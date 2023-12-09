# Import BeautifulSoup for HTML parsing
from bs4 import BeautifulSoup

# Function to read and parse the HTML content from the file
def get_html_content():
    # Open and read the HTML file
    with open('templates/Agentlogin.html', 'r') as file:
        # Read the content and parse it using BeautifulSoup
        html_content = file.read()
        return BeautifulSoup(html_content, 'html.parser')

# Test case to check if the title exists and has the expected text
def test_title_exists_and_text():
    # Get the parsed HTML content
    soup = get_html_content()
    # Find the title tag
    title_tag = soup.find('title')
    # Assert that the title tag exists
    assert title_tag is not None
    # Assert that the text of the title tag is as expected
    assert title_tag.text.strip() == 'SFS Agent Login'

# Test case to check the presence and attributes of the form elements
def test_login_form_elements():
    # Get the parsed HTML content
    soup = get_html_content()
    # Find the form tag
    form = soup.find('form')
    # Assert that the form tag exists
    assert form is not None

    # Find the username input field
    username_input = form.find('input', {'id': 'username', 'name': 'username'})
    # Assert that the username input field exists
    assert username_input is not None
    # Assert that the placeholder attribute is as expected
    assert username_input['placeholder'] == 'User name'

    # Find the password input field
    password_input = form.find('input', {'id': 'password', 'name': 'password'})
    # Assert that the password input field exists
    assert password_input is not None
    # Assert that the placeholder and type attributes are as expected
    assert password_input['placeholder'] == 'password'
    assert password_input['type'] == 'password'

    # Find the submit button
    submit_button = form.find('button')
    # Assert that the submit button exists
    assert submit_button is not None
    # Assert that the text of the submit button is as expected
    assert submit_button.text.strip() == 'Login'

# Test case to check if the image tag for the logo exists
def test_logo_image_exists():
    # Get the parsed HTML content
    soup = get_html_content()
    # Find the image tag with the specified alt attribute
    img_tag = soup.find('img', {'alt': 'logo SFS'})
    # Assert that the image tag exists
    assert img_tag is not None
    # Assert that the src attribute is as expected
    assert img_tag['src'] == 'static/logo.png'

# Test case to check if the JavaScript file is linked
def test_js_file_linked():
    # Get the parsed HTML content
    soup = get_html_content()
    # Find the script tag with the specified src attribute
    script_tag = soup.find('script', {'src': "{{ url_for('static', filename='index.js') }}"})
    # Assert that the script tag exists
    assert script_tag is not None

# Test case to check if the CSS file is linked
def test_css_file_linked():
    # Get the parsed HTML content
    soup = get_html_content()
    # Find the link tag with the specified href attribute
    link_tag = soup.find('link', {'href': "{{ url_for('static', filename='style2.css') }}"})
    # Assert that the link tag exists
    assert link_tag is not None
