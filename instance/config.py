
""" contains links to database connections, ie.,mysql
    mail client, ie.gmail, yahoo,
    also hold the secret key used wit form validations
"""

class Config:
    SECRET_KEY = 'c7c52ced176b65114f3e211f'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://MUSTAFA:5m9l<18>_X!@localhost/Automobile'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True