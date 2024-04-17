
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

    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000000) # defines the code to the default budget money
    
    role = db.relationship('Roles', backref='users')
    vehicle = db.relationship('Vehicles', backref='owned_user', lazy=True)

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
    
    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)

        if user:
            # Disassociate all vehicles owned by the user
            vehicles_owned_by_user = Vehicles.query.filter_by(owner=user.id).all()
            
            for vehicle in vehicles_owned_by_user:
                vehicle.owner = None
            db.session.commit()
            
            # Now you can safely delete the user
            db.session.delete(user)
            db.session.commit()
            return True
        else:
            return False



class Roles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    role_name = db.Column(db.String(length=30), nullable=False, unique=True)

   

# data contained in the server's database
class Vehicles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    model = db.Column(db.String(length=60), nullable=False, unique=False)
    price = db.Column(db.Integer(), nullable=False) 
    description = db.Column(db.String(length=1024), nullable=False)
    car_type = db.Column(db.String(length=30), unique=False)
   
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

   
    def __repr__(self):
        return f'Item {self.model}'

    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    # def sell(self, user):
    #     self.owner = None
    #     user.budget += self.price
    #     db.session.commit()
    
    