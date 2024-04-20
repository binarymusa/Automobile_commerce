
from Automobile import db,login_manager
from Automobile import bcrypt
from flask_login import UserMixin
import re


# tells Flask-Login that the function (load_user) should be used to retrieve a user object when a user is logged in and their session needs to be managed.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# data fetched from the user
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True) # primary-key column named id
    user_role = db.Column(db.Integer(), db.ForeignKey('roles.id'))

    username = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000000) # defines the code to the default budget money
    
    role = db.relationship('Roles', backref='users')
    cart_relationship = db.relationship('Cart', backref='users', lazy=True)
    purchased_relationship = db.relationship('PurchasedItems', backref='users', lazy=True)
    # vehicle = db.relationship('Vehicles', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            # unfinished items here
            return f'{self.budget}'
        else:
            return f"{self.budget}"
    
    @property
    def password(self):
        return self.password

    @password.setter
    # hashes the password using bcrypt and stores the hashed value in the "password_hash" column.
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    # check if a provided plain-text password matches the hashed password stored in the "password_hash" column
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    
    def can_purchase(self, vehicle_obj):
        return self.budget >= vehicle_obj.price
    
    def can_sell(self, vehicle_obj):
        return vehicle_obj in self.vehicle
    

    # function to set the admin budget to 0 else other value
    @staticmethod
    def Admin_budget():
        users = User.query.filter_by(user_role=1).all()
        
        if users:
            for user in users:
                user.budget = 0
            db.session.commit()
            return f"Budget of user with ID  has been set to zero."
        else:
            return 'No users found with the specified role.'


    #function to dissasociate a user with a car
    @staticmethod
    def dissasociate_user_car(user_id):        
        user = User.query.get(user_id)

        if user:
            # Disassociate all vehicles owned by the user
            # Combine cart items and purchased items into a single query result
            vehicles_owned_by_user = Cart.query.filter_by(user_id=user_id).union(
                PurchasedItems.query.filter_by(user_id=user_id)
            ).all()
            
            for vehicle in vehicles_owned_by_user:
                vehicle.owner = None

            user.budget = 1000000
            db.session.commit()
            
            return True
        else:
            return False

    # function to dissasociate a user with a car before deleting them
    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        
        if user :
            # Subquery to select vehicle IDs owned by the user
            # A subquery is simply a nested query. can be used in another query
            subquery = db.session.query(Cart.id).filter_by(user_id=user_id).union(
                db.session.query(PurchasedItems.id).filter_by(user_id=user_id)
            ).subquery()
            
            # Delete related records from Cart and PurchasedItems tables and disassociate vehicles
            Cart.query.filter(Cart.id.in_(subquery)).delete(synchronize_session=False)
            PurchasedItems.query.filter(PurchasedItems.id.in_(subquery)).delete(synchronize_session=False)

            # Now you can safely delete the user
            db.session.delete(user)
            db.session.commit()
            return True
        else:
            return False


# maps user roles
class Roles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    role_name = db.Column(db.String(length=30), nullable=False, unique=True)

   
# Vehhicles as contained in the server's database
class Vehicles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    model = db.Column(db.String(length=60), nullable=False, unique=False)
    price = db.Column(db.Integer(), nullable=False) 
    description = db.Column(db.String(length=1024), nullable=False)
    car_type = db.Column(db.String(length=30), unique=False)
    # car_units = db.Column(db.Integer(), nullable=False, unique=False)
   
    # owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    cart_relationship = db.relationship('Cart', backref='vehicle', lazy=True)
    purchased_relationship = db.relationship('PurchasedItems', backref='vehicle', lazy=True)

   
    def __repr__(self):
        return f'Item {self.model}'
    
    def add_to_cart(self, user):
        cart_item = Cart(user_id=user.id, vehicle_id=self.id)
        self.owner = user.id
        db.session.add(cart_item)
        db.session.commit()


    def buy(self, user):
        purchased_item = PurchasedItems(user_id=user.id, vehicle_id=self.id)
        self.owner = user.id
        user.budget -= self.price
        db.session.add(purchased_item)
        db.session.commit()

   

class Cart(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    
    vehicle_id = db.Column(db.Integer(), db.ForeignKey('vehicles.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def remove_from_cart(self):
        db.session.delete(self)
        db.session.commit()

class PurchasedItems(db.Model):
    id = db.Column(db.Integer(), primary_key=True)

    vehicle_id = db.Column(db.Integer(), db.ForeignKey('vehicles.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    