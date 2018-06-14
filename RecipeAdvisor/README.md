# CS530-Developing-User-Interfaces
Final project, a recipe advisor

# Project Title 
TIRED OF FINDING WHAT TO COOK? WE KNOW WHAT YOU WANT MORE THAN YOU, A Recipe Advisor. 

# Getting Started 
This project, done as the final project of CS 530 (Developing User Interfaces), suggest a recipe based on 5 predefined features, moreover allows the user to search thorough all recipes by an advanced search option. Available at  http://129.25.26.35:8000/core/index/ in Drexel Network. 
The web-based files are written using html, CSS, bootstrap and JavaScript. And the database is PostgreSQL. Our server is on Pycharm framework and the relation with the database is done by Django ORM. 
If you want to run it on your local machine, you should follow the instructions below, and take in mind that your database would be empty in this case.  

# Attached Folder's content 
+Recipe_advisor (project directory) 
+Core (containing the html files in the template folder, besides to urls.py and view.py ) 
+Recipe_advisor (containing the setting of the server and the first url file)  
+Static (all static data such as style.css file and images that are used in the application) 
-Manage.py 

# Prerequisites 
Copy all database and other code related parts in the attached folder to a directory, which would be used in the following steps.
Requests 
Python 2 
python-pip 
python-dev 
python -m pip install django psycopg2 
Postgres  
(fully described at https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) 

# Deployment and Installing 
Copy all database and other code related part to a directory, which is used in previouse steps 
You should keep in mind that whenever there is a database change resolved, you have to run this command in the terminal. 
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver 

And then run your server, which is probably http://127.0.0.1:8000/admin/. If you see a profile, everything is done correctly. This environment helps you to fill the database. 
Also at http://127.0.0.1:8000/core/index/, you should see the main page of the application. 

# Author 
Maryam Daniali, CS530, Spring 2018. 

 
