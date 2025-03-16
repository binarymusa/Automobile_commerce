import unittest
from Automobile import app,db
from Automobile.models import User

""" unfinished """
class TestRoutes(unittest.TestCase):

    # Define a setUp method to be executed before each test method
    def setUp(self):
        # Create a test client for the Flask app
        self.app = app.test_client()
        
        # Set up the Flask application context and create a test database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://MUSTAFA:5m9l<18>_X!@localhost/Automobile'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.create_all()
        self.app_context = app.app_context()
        self.app_context.push()

    # test method for the login page
    def test_login_page(self):
        # Send a GET request to the login page
        response = self.app.get('/login_page')
        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Assert that the response data contains the word "Login"
        self.assertIn(b'Login', response.data)


    def test_sign_up(self):
        response = self.app.get('/sign_up_page')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    # test method for the market page
    def test_market_page(self):
        response = self.app.get('/market_page')
        # Assert that the response status code is 302 (Redirect)
        self.assertEqual(response.status_code, 302)
        self.assertIn(b'Location: http://127.0.0.1/', response.data)

    def test_filter_page(self):
        response = self.app.get('/filter_page')
        self.assertEqual(response.status_code, 302)
        self.assertIn(b'Location: http://127.0.0.1/', response.data)

    def test_cart_page(self):
        response = self.app.get('/mycart_page')
        self.assertEqual(response.status_code, 302)
        self.assertIn(b'Location: http://127.0.0.1/', response.data)

    def test_purcahse_page(self):
        response = self.app.get('/mycart_page')
        self.assertEqual(response.status_code, 302)
        self.assertIn(b'Location: http://127.0.0.1/', response.data)

    def test_database_connection(self):
        # Test database connection using query
        """ user = User(username='duke', email_address='duke@hotmail.com', phone_no='0912345678', password_hash='12345')
        db.session.add()
        db.session.commit() """
        queried_user = User.query.filter_by(username='duke').first()

        if not queried_user:
            new_user = User(username='duke', 
                            email_address='duke@hotmail.com', 
                            phone_no='0912345678', 
                            password_hash='12345'
                            )
            db.session.add(new_user)
            db.session.commit()
        else:
            queried_user.email_address = 'duke@gmail.com'
            db.session.delete(queried_user)
            db.session.commit()
       
        self.assertIsNotNone(queried_user)
        self.assertEqual(queried_user.email_address, 'duke@hotmail.com')


if __name__ == '__main__':
    unittest.main()
