
""" contains links to database connections, ie.,mysql
    mail client, ie.gmail, yahoo,
    also hold the secret key used wit form validations
"""

import os

class Config:
    SECRET_KEY = '89cf297f4b4634754cd052c1'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://MUSTAFA:5m9l<18>_X!@localhost/Automobile'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True