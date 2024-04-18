
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

         if check_user.role and check_user.role.role_name == 'Admin':
            flash(f'Admin Login successful', category='success')
            return redirect(url_for('admin_welcome'))
         else:
            flash(f'Login successful', category='success')
            return redirect(url_for('welcome_page'))
      else:
         flash(f'Username and Password  mismatch', category='danger')
         return redirect(url_for('login_page'))
  
   else:
      return render_template('login.html')


@app.route('/Admin_welcome_page')
def admin_welcome():
   return render_template('welcome_adm.html')

@app.route('/Admin_page', methods=['GET' , 'POST'])
@login_required
def admin_page():
   users = User.query.filter(User.id != 6).all()
   
   if request.method == 'POST':
      user_to_delete = request.form['user_delete']

      if user_to_delete:
        User.delete_user(user_to_delete)

        flash('user deletion confirmed', category='danger')
        return redirect(url_for('admin_page'))  

   return render_template('admin.html', users =users, )


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


@app.route('/market_page', methods=['GET', 'POST'])
@login_required
def market_page():
   mercedes = Vehicles.query.filter_by(car_type='mercedes').all()
   bmw = Vehicles.query.filter_by(car_type='bmw').all()
   rover = Vehicles.query.filter_by(car_type='rangerover').all()
   audi = Vehicles.query.filter_by(car_type='audi').all()

   combined_items = zip(mercedes, bmw, rover, audi)

   
   if request.method == 'POST':
      item = request.form.get('purchased_vehicle')  #['purchased_vehicle']
      item2 = request.form.get('added_vehicle') #['added_vehicle']
      
      if item:
         selected_item = Vehicles.query.filter_by(id=item).first()
         
         if selected_item and selected_item.owner == None:
            if current_user.can_purchase(selected_item):
               selected_item.buy(current_user)
               flash('purchase was successful', category='success')
               return redirect(url_for('purchases_page'))
            else:
               flash('you dont enough money to make purchase')
         else:
            flash('Vehicle currently unavailable', category='danger')

      elif item2:
         selected_item = Vehicles.query.filter_by(id=item2).first()

         if selected_item and selected_item.owner == None:
            # Add logic to add the item to the cart
            selected_item.add_to_cart(current_user)
            
            flash('Item added to cart', category='success')
            return redirect(url_for('cart_page'))
         else:
            flash('Vehicle currently unavailable', category='danger')

      
   return render_template('Market.html', mercedes=mercedes,bmw=bmw,rover=rover,audi=audi, combined_items = combined_items)


@app.route('/mycart_page')
@login_required
def cart_page():
   my_cart = Vehicles.query.filter_by(owner=current_user.id).all()

   return render_template('Cart.html', my_cart=my_cart )

@app.route('/my_purchases_page')
@login_required
def purchases_page():
   my_purchase = Vehicles.query.filter_by(owner=current_user.id).all()


   return render_template('purchased.html', my_purchase=my_purchase)


@app.route('/logout')
def logout_page():
   logout_user()
   flash(" logged out succesfully!", category='info')
   return redirect(url_for('login_page'))