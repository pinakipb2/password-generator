# Random Strong Password Generator in Python using Flask
# Made by Pinaki
from flask import Flask, render_template, redirect, url_for, request, flash
import string
import random

app = Flask(__name__)
app.secret_key = 'v?>N|dznLDsYkby5EV!Z' # This key is generated using this app

@app.route('/',methods=['GET','POST'])
def home():
    sec_pass = 0
    if request.method == 'POST':
        password = int(request.form.get('password'))
        if (password<8 and password>94):
            flash("Password length must be greater than 8 and less than 128",'warning')
        else:
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = string.punctuation
            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            sec_pass = ("".join(random.sample(s,password)))
    return render_template('index.html',sec_pass=sec_pass)

if __name__ == '__main__':
    app.run(debug=True)