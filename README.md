The PROJECT covers an Automobile e-comerce site based on flask.

Files in the app include :

  STATIC FILES(includes css,html templates, javascript and images used)
  
  INIT FILE
  
  FORMS, MODELS(databse tables)
  
  VIEWS file(or the routes page)
  
  REQUIREMENTS FILES(contains file dependencies)
  
  and a RUN.PY file for firing up the app
      
Follow the below steps to run the app:
Ensure you have a version of python installed.

In the run.py file, give the port number that is free for your computer

To execute the app, open the directory in the terminal and write the code:

  python run.py or python3 run.py

using a wsgi server such as gunicorn with nginx :
    gunicorn -w 4 -b 0.0.0.8000 run:app
