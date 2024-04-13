
from Automobile import app
from flask import redirect, url_for, render_template, flash, session,request
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/login_page')
def login_page():
   return render_template('login.html')


@app.route('/welcome_page')
def welcome_page():
   return render_template('Welcome.html')


@app.route('/sign_up_page')
def signup_page():
   
   return render_template('signup.html')

@app.route('/market_page', methods=['POST', 'GET'])
# @login_required
def market_page():
   return render_template('Market.html')


@app.route('/mycart_page')
# @login_required
def cart_page():
   return render_template('Cart.html')


@app.route('/logout')
def logout_page():
   logout_user()
   flash(" logged out succesfully!", category='info')
   return redirect(url_for('Welcome_page'))