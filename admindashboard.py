from flask import Flask, render_template

app = Flask(__name__)

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
