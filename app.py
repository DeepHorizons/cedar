from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/signup', methods = ['POST'])
def signup():
    email=request.form['email']
    print("the email address is '" +email+ "'")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
