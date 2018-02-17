from flask import Flask, render_template, redirect, request, g
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods = ['POST'])
def signup():
    email=request.form['email']
    print("the email address is '" +email+ "'")
    g.db.execute("INSERT INTO email_addresses VALUES (?)", [email])
    g.db.commit()
    return redirect('/')

@app.before_request
def before_request():
    g.db = sqlite3.connect("emails.db")

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
@app.route('/email.html')
def emails():
    email_addresses = g.db.execute("SELECT email FROM email_addresses").fetchall()
    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == '__main__':
    app.run(debug=True)
