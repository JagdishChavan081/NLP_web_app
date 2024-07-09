from flask import Flask, render_template, request, redirect 
from db import Database
import api

app = Flask(__name__)

dbo = Database()

@app.route('/')
def index():
   
    return render_template('login.html')
 
@app.route('/register')
def register():
    return render_template('register.html')

#perform registration ->pr
@app.route('/pr', methods=['post'])
def pr():
    #fetching data from register.html
    name=request.form.get('user_name')
    email=request.form.get('user_email')
    password=request.form.get('user_password')

    #inserting data into database
    responce = dbo.insert(name=name,email=email,password=password)

    if responce:
        return render_template('login.html',message="Registration Successful,login to proceed")
    else:
        return render_template('register.html',message="email already exists")


#perform login ->pl
@app.route('/pl',methods=['post'])
def pl():

    #feching data from login.html
    email=request.form.get('user_email')
    password=request.form.get('user_password')

    responce=dbo.search(email=email,password=password)

    if responce :
        return redirect('/profile')
    else:
        return render_template('login.html', message='incorrect email/password')
    
#profile page
@app.route('/profile')
def profile():
    return render_template('profile.html')
    

#NER-Services
@app.route('/ner')
def ner():
    return render_template('ner.html')
  

#perform ner -> pner
@app.route('/p_ner', methods=['post'])
def p_ner():
    text = request.form.get('ner_text')
    responce=api.ner(text)
    print(responce)
    return render_template('ner.html', responce=responce)
    



app.run(debug=True)