
from Automobile import app,db
from flask import redirect, url_for, render_template, flash, session,request
from flask_login import login_user, logout_user, login_required, current_user
from Automobile.models import User, Vehicles


@app.route('/')
@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']

      check_user = User.query.filter_by(username=username).first()

      if check_user and check_user.check_password_correction(attempted_password=password):
         login_user(check_user) 
         flash(f'Login successful', category='success')
         return redirect(url_for('welcome_page'))
      else:
         flash(f'Username and Password  mismatch', category='danger')
         return redirect(url_for('login_page'))
  
   else:
      return render_template('login.html')


@app.route('/welcome_page')
def welcome_page():
   return render_template('Welcome.html')


@app.route('/sign_up_page' , methods=['GET', 'POST'])
def signup_page():
   if request.method == 'POST':
      # Get data from the form
      username = request.form['username']
      email = request.form['email']
      password = request.form['password']
         

      existing_user = User.query.filter((User.username == username) | (User.email_address == email)).first()
      
      if existing_user:
         flash(f'User already exists. Try different credentials',category='danger')
         return redirect(url_for('signup_page'))
      else:
         # Add the new user to the database
         new_user = User(username=username, email_address=email, password=password)
         db.session.add(new_user)
         db.session.commit()

      login_user(new_user)
      flash(f'signup successful', category='success')
      # Redirect to a success page or do whatever you want after signup
      return redirect(url_for('welcome_page'))
   else:
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
   return redirect(url_for('login_page'))