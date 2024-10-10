
from Automobile import app,db
from flask import redirect, url_for, render_template, flash, session,request
from flask_login import login_user, logout_user, login_required, current_user
from Automobile.models import User, Vehicles, Cart, PurchasedItems
from sqlalchemy import or_, and_
import re

@app.route('/')
@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
   if request.method == 'POST':
      username = request.form['username']
      password = request.form['password']

      check_user = User.query.filter_by(username=username).first()

      if check_user and check_user.check_password_correction(attempted_password=password):
         login_user(check_user) 

         #  Access the associated role object via the role relationship
         if check_user.role and check_user.role.role_name == 'Admin':
            flash(f'Admin Login successful', category='success')
            return redirect(url_for('admin_welcome'))
         else:
            flash(f'Login successful', category='success')
            return redirect(url_for('welcome_page'))
      else:
         flash(f'Incorrect username or Password', category='danger')
         return redirect(url_for('login_page'))
  
   else:
      return render_template('login.html')

@app.route('/sign_up_page' , methods=['GET', 'POST'])
def signup_page():
   if request.method == 'POST':
      # Get data from the form
      username = request.form['username']
      email = request.form['email']
      password = request.form['password']
         
      existing_user = User.query.filter(and_(User.username == username , User.email_address == email)).first()
      
      if existing_user:
         flash(f'User already exists. Try different credentials', category='danger')
         return redirect(url_for('signup_page'))
      else:
         #checks if the email given matches the expression 
         reg_exp = '^\S+(\@gmail\.com$|\@hotmail\.com$|\@yahoo\.com$)$'
         try:
            if (not(re.search(reg_exp, email))):
               flash('Invalid email address!', category='danger')
               return redirect(url_for('signup_page'))
            else:
               # return True
               print(email)           
               # Add the new user to database
               new_user = User(username=username, email_address=email, password=password)
               db.session.add(new_user)
               db.session.commit()

               login_user(new_user)
               flash(f'signup successful', category='success') 
               return redirect(url_for('welcome_page'))     
         except:
            flash('an error occured', category='danger')

      return render_template('signup.html')
   else:
      return render_template('signup.html')


@app.route('/Admin_welcome_page')
def admin_welcome():
   return render_template('includes/welcome_adm.html')

@app.route('/Admin_page', methods=['GET' , 'POST'])
@login_required
def admin_page():   
   # '|' , or_ - represents 'or' logical operator
   # check for users with roles other than 1 and null roles and pass them to query for display
   # users = User.query.filter((User.user_role != 1) | (User.user_role == None)).all()
   query_items = (
      User.query.filter(or_(User.user_role != 1 , User.user_role == None)).all(),
      Cart.query.all(), 
      PurchasedItems.query.all(), 
      Vehicles.query.all()
   )

   if request.method == 'POST':
      user_to_delete = request.form.get('user_delete')
      vehicle_to_delete = request.form.get('vehicle_delete')

      if user_to_delete:
        User.delete_user(user_to_delete)

        flash('user deletion confirmed', category='danger')
        return redirect(url_for('admin_page'))  
           
      elif vehicle_to_delete:
         selected_vehicle = Vehicles.query.filter_by(id=vehicle_to_delete).first()

         if selected_vehicle:
            selected_vehicle.delete_vehicle()
            flash('vehicle deletion succesful', category='danger')
            return redirect(url_for('admin_page'))
         else:
            flash('deletion unsuccesful', category='danger')


   return render_template('admin.html', query_items = query_items )


@app.route('/Admbook_page', methods=['GET' , 'POST'])
@login_required
def admin_page2(): 
   
   return render_template('adm_book.html')

@app.route('/welcome_page')
def welcome_page():
   return render_template('includes/Welcome.html')

@app.route('/AddVehicle_page', methods=['GET' , 'POST'])
def add_vehicle_page():
   if request.method == 'POST':
      items = [
         request.form['price'], request.form['description'],
         request.form['model'], request.form['type'], request.form['link'], 
         request.form['units'], request.form['year']
      ]
      print(items[5])
      print(0>int(items[5]))

      if items:
         reg_exp = '^\d{4}$'
         try:
            if (not(re.search(reg_exp, items[6]))):
               flash('invalid year or car units!',category='danger')
               return(redirect(url_for('add_vehicle_page')))
            else:
               new_vehicle = Vehicles(
                  price=items[0], description=items[1],
                  model=items[2], car_type=items[3], 
                  image_link=items[4], vehicle_units=items[5], 
                  year=items[6]
               ) 
               db.session.add(new_vehicle)
               db.session.commit()
               return redirect(url_for('admin_page'))
         except:
            flash('An error occurred!', category='danger')
   else:
      return render_template('includes/addVeh.html')


@app.route('/market_page', methods=['GET', 'POST'])
@login_required
def market_page():
   car_types = ['mercedes', 'bmw', 'rangerover', 'audi']

   # Using dictionary comprehension to store the results for each car type
   cars_by_type = {car_type: Vehicles.query.filter_by(car_type=car_type).all() for car_type in car_types}
   # print(cars_by_type)
   
   if request.method == 'POST':
      item = request.form.get('purchased_vehicle') 
      item2 = request.form.get('added_vehicle') 
                  
      if item:         
         selected_item = Vehicles.query.filter_by(id=item).first()     
         
         if selected_item and selected_item.vehicle_units > 0:            
            if current_user.can_purchase(selected_item):
               selected_item.buy(current_user)
               flash('purchase was successful', category='success')
               return redirect(url_for('purchases_page'))
            else:
               flash('Not enough money to make purchase', category='danger')
         else:
            flash('Vehicle sold out', category='danger')

      elif item2:
         selected_item = Vehicles.query.filter_by(id=item2).first()  
                
         if selected_item and selected_item.vehicle_units > 0:
            # Add item to the cart based on method in its model
            selected_item.add_to_cart(current_user)
            
            flash('Item added to cart', category='success')
            return redirect(url_for('cart_page'))
         else:
            flash('Vehicle currently unavailable', category='danger')

   return render_template('Market.html', cars_by_type=cars_by_type)


@app.route('/filter_page', methods=['GET', 'POST'])
@login_required
def filtered_page():   
   if request.method == 'POST': 
      filtered = (
         request.form['model'], 
         request.form['price'], 
         # request.form['price2'],
         request.form['year']
      )
     
      items = (filtered[0] , filtered[1], filtered[2])
      
      for item in items:
         print(item, type(item))   

      filter_criteria = Vehicles.query.filter(
         (and_(Vehicles.car_type == filtered[0], Vehicles.price == filtered[1], Vehicles.year == filtered[2]))
           | 
         (or_(Vehicles.car_type == filtered[0], Vehicles.price == filtered[1], Vehicles.year == filtered[2]))
           |
         (and_(Vehicles.car_type == filtered[0], Vehicles.price == filtered[1]))
           |
         (and_(Vehicles.car_type == filtered[0], Vehicles.year == filtered[2]))
           |
         (and_(Vehicles.price == filtered[1], Vehicles.year == filtered[2])) 
                                   
      ).all()          
       
      if filtered and filter_criteria:         
         print(filter_criteria)         
         return render_template('includes/filtered.html', filtered_items= filter_criteria)
      else:
         flash('no matching results!', category='danger')
        
   return render_template('includes/filtered.html',)


@app.route('/mycart_page', methods=['GET', 'POST'])
@login_required
def cart_page():

   if request.method == 'GET':
      my_cart = Cart.query.filter_by(user_id=current_user.id).all()
      
      # Initialize a list to store the details of each vehicle in the cart
      cart_vehicle_details = []

      for item in my_cart:         
         vehicle = item.vehicle  # Access the associated vehicle object via the relationship
         # Add the details of the vehicle to the list
         cart_vehicle_details.append({
            'id': vehicle.id,
            'model': vehicle.model,
            'price': vehicle.price,
            'description': vehicle.description,
            'car_type': vehicle.car_type,
            'car_image': vehicle.image_link
         
         })
      length_of_list = len(cart_vehicle_details)       

   if request.method == 'POST':
      item = request.form.get('buy_added_vehicle')
      item2 = request.form.get('remove_added_vehicle')

      if item:            
         selected_vehicle = Cart.query.filter_by(vehicle_id=item).first()
         print(selected_vehicle)

         if selected_vehicle and current_user.can_purchase(selected_vehicle.vehicle):
            selected_vehicle.vehicle.buy(current_user)

            flash('Purchase was successful', category='success')
            # After purchasing, remove the item from the cart
            cart_item = Cart.query.filter_by(vehicle_id=item, user_id=current_user.id).first()
            
            db.session.delete(cart_item)
            db.session.commit()
            return redirect(url_for('purchases_page'))
         else:
            flash('Not enough money to purchase', category='danger')
            return redirect(url_for('cart_page'))
   
      elif item2:
         selected_vehicle = Cart.query.filter_by(vehicle_id=item2, user_id=current_user.id).first()
         
         if selected_vehicle:
            selected_vehicle.remove_from_cart()
            flash('item removed from cart', category='success')
            return redirect(url_for('cart_page'))
         else:
            flash('an error occured', category='danger')      

   return render_template('Cart.html', cart_vehicle_details=cart_vehicle_details, length_of_list = length_of_list)


@app.route('/my_payment')
@login_required
def payment_page():
   return render_template('includes/payment.html')


@app.route('/my_purchases', methods=['GET', 'POST'])
@login_required
def purchases_page():
   if request.method == 'GET':
      my_purchase = PurchasedItems.query.filter_by(user_id=current_user.id).all()
      
      # Initialize a list to store the details of each vehicle in the cart
      purchased_vehicle_details = []

      # Iterate over each item in the cart and retrieve the details of the associated vehicle
      for item in my_purchase:
         vehicle = item.vehicle
         
         purchased_vehicle_details.append({
            'id': vehicle.id,
            'model': vehicle.model,
            'price': vehicle.price,
            'description': vehicle.description,
            'car_type': vehicle.car_type,
            'car_image': vehicle.image_link
         })
   
   return render_template('purchased.html', purchased_vehicle_details=purchased_vehicle_details)


@app.route('/logout')
def logout_page():
   logout_user()
   flash(" logged out succesfully!", category='info')
   return redirect(url_for('login_page'))