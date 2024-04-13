
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
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=10000000) # defines the code to the default budget money
    

    items = db.relationship('Vehicles', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
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
    
    """ def check_email_validity(self, email_address):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
        # Check if the provided email matches the pattern
        if re.match(email_regex, email_address):
            return True
        else:
            return False """
            
   

# data contained in the server's database
class Vehicles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    model = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    Dealership = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)
   

    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    
    