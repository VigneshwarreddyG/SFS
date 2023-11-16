from bs4 import BeautifulSoup

# Function to read and parse the HTML content from the file
def get_html_content():
    with open('templates/Agentlogin.html', 'r') as file:
        html_content = file.read()
        return BeautifulSoup(html_content, 'html.parser')

# Test case to check if the title exists and has the expected text
def test_title_exists_and_text():
    soup = get_html_content()
    title_tag = soup.find('title')
    assert title_tag is not None
    assert title_tag.text.strip() == 'SFS Agent Login'

# Test case to check the presence and attributes of the form elements
def test_login_form_elements():
    soup = get_html_content()
    form = soup.find('form')
    assert form is not None

    username_input = form.find('input', {'id': 'username', 'name': 'username'})
    assert username_input is not None
    assert username_input['placeholder'] == 'User name'

    password_input = form.find('input', {'id': 'password', 'name': 'password'})
    assert password_input is not None
    assert password_input['placeholder'] == 'password'
    assert password_input['type'] == 'password'

    submit_button = form.find('button')
    assert submit_button is not None
    assert submit_button.text.strip() == 'Login'

# Test case to check if the image tag for the logo exists
def test_logo_image_exists():
    soup = get_html_content()
    img_tag = soup.find('img', {'alt': 'logo SFS'})
    assert img_tag is not None
    assert img_tag['src'] == 'static/logo.png'

# Test case to check if the JavaScript file is linked
def test_js_file_linked():
    soup = get_html_content()
    script_tag = soup.find('script', {'src': "{{ url_for('static', filename='index.js') }}"})
    assert script_tag is not None

# Test case to check if the CSS file is linked
def test_css_file_linked():
    soup = get_html_content()
    link_tag = soup.find('link', {'href': "{{ url_for('static', filename='style2.css') }}"})
    assert link_tag is not None


