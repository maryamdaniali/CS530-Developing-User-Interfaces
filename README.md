# CS530-Developing-User-Interfaces
Final course project, a recipe advisor
[![Project demo](https://www.cs.drexel.edu/~md3464/Projects/2110d430eae79bbaa0bffdd9eb7f4e18.jpg)](https://www.youtube.com/watch?v=lTkf1b2QHnQ "- Click to Watch!")
# Project Title 
TIRED OF FINDING WHAT TO COOK? WE KNOW WHAT YOU WANT MORE THAN YOU! 
### a *Recipe Advisor*!

# Getting Started 
This project suggests a recipe to users based on 5 predefined features. Moreover, it allows users to search among all recipes by an advanced search option.  
The web-based files are written using html, CSS, bootstrap and JavaScript, and the database is created using PostgreSQL. Our server is on Pycharm framework, and the relation with the database is done by Django ORM. 

If you want to run it on your local machine, you should follow the instructions below and keep in mind that your database would be empty in this case.  

# Contents 
+Recipe_advisor (project directory) 
+Core (containing the html files in the template folder, besides urls.py and view.py ) 
+Recipe_advisor (containing the setting of the server and the first url file)  
+Static (all static data such as style.css file and images that are used in the application) 
-Manage.py 

# Prerequisites 
Clone the repository or manually copy the database and code to a local directory. Follow the 
Requirements:

 - Requests 
 - Python 2  
 - pip  
 - python-dev  
 - Postgres
 - django
 
 You can install `django` using the command below:
```bash
python -m pip install django psycopg2
```
 For more information about Django please see [this](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) tutorial. 
# Deployment and Installing 
Clone the repository to a local directory that has access to the previously mentioned requirements. 
You should keep in mind that whenever there is a database change resolved, you need to run the following commands to get the latest changes.
``` bash
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver 
```
Then run your server, which by default is on http://127.0.0.1:8000/admin/. If you see a profile, everything is done correctly. This environment helps you to fill out the database. 
You can access the main page of the application on http://127.0.0.1:8000/core/index/.

# Author 
Maryam Daniali (CS 530: Developing User Interfaces, Spring 2018) 

 
