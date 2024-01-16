# Online Bookstore

This is a simple online bookstore web application built using Python and Flask.

## Features

- Display a catalog of books with details such as title, author, genre, price, and cover image.
- Search for books by title or author.
- Add books to a shopping cart.
- View the contents of the shopping cart.
- Clear the entire shopping cart.

## Prerequisites

- Python installed (version 3.6 or higher)
- Flask framework

## How to RUN

1. Checkout the project from git
2. On CMD navigate to the project directory
4. Execute "python app.py"
5. Open your web browser and visit http://127.0.0.1:5000/ to access the online bookstore.

## Usage

- Navigate to the home page to view the catalog of books.
- Use the search functionality to find specific books by title or author.
- Click "Add to Cart" to add a book to your shopping cart.
- View your shopping cart by clicking on the "Cart" link.
- Clear your entire shopping cart by clicking the "Clear Cart" button.

# Deployment Method: PythonAnywhere (using web interface)

## How to deploy a Flask App using PythonAnywhere

## Step 1: Create a PythonAnywhere account
If you don't have an account on PythonAnywhere, sign up at PythonAnywhere. Then login.

## Step 2: Create a new web app
From your PyhtonAnywhere Dashboard, go to 'Web' tab. Click on 'Add a new web app' and then click 'next' > choose 'Flask' for the Python Web framework > select Python version 'Python 3.10 (Flask 2.1.2)' > click 'next'.

## Step 3: Using a virtualenv in your web app (to get newer versions of flask)
You can use a virtualenv in a new web app (created using the “Manual configuration” option) or in your existing web apps. To use a virtualenv in your web app, do the following:
	1.	Create a virtualenv
	2.	Install packages into your virtualenv
	3.	Configure your app to use this virtualenv
	
From the dashboard, got to the 'Consoles' tab, then click on 'Bash' to start your Bash console.
We recommend using virtualenvwrapper, a handy command-line tool, to create your virtualenv.
Specify which Python version to use for your virtualenv using the --python option, but note that it must match the version of Python you've chosen for your web app. So, to create a new Python 3.10 virtualenv, run this command:
'mkvirtualenv myvirtualenv --python=python3.10' 
Once your virtualenv is ready and active, you’ll see (myvirtualenv) $ in your prompt.
Whenever you want to work on your project in the console, you need to make sure the virtualenv is active. You can reactivate it at a later date with typing 'workon my-virtualenv' in the bash console.

## Step 4: Install packages/dependencies into your virtualenv
	pip install flask
	pip install flask-sqlalchemy
	pip install flask-login
	
## Step 5: Upload Flask app
Head to the 'Files tab', go to 'mysite/'. Remove the placeholder file in there (myflask.py).
Upload your files one by one into the mysite/ folder. Your file folder structure should look like this:
.
└── mysite
    ├── __pycache__
    │   ├── app.cpython-310.pyc
    │   └── flask_app.cpython-310.pyc
    ├── app.py
    ├── instance
    │   └── site.db
    ├── site.db
    ├── static
    │   ├── images
    │   │   ├── book_cover (1).jpg
    │   │   ├── book_cover (10).jpg
    │   │   ├── book_cover (2).jpg
    │   │   ├── book_cover (3).jpg
    │   │   ├── book_cover (4).jpg
    │   │   ├── book_cover (5).jpg
    │   │   ├── book_cover (6).jpg
    │   │   ├── book_cover (7).jpg
    │   │   ├── book_cover (8).jpg
    │   │   └── book_cover (9).jpg
    │   └── styles.css
    └── templates
        ├── cart.html
        ├── index.html
        ├── login.html
        ├── logout.html
        ├── purchase_error.html
        ├── purchase_success.html
        ├── search_results.html
        └── signup.html

## Step 6: Configuring your Flask app
Go to 'Web' tab, click on 'WSGI configuration file', and then change this line of code 'from app import app as application' to 'from flask_app import app as application'. 
This needs to be done since our app name is app.py.

## Step 7: Linking the virtual environment
Go to Web tab, and then scroll down to virtualenv section. Click on 'Enter path to a virtualenv, if desired' and enter 'myvirtualenv' to define our virtual environment path.
Scroll up and then click Reload

## Step 8: Visiting the link of the deployed Flask app
In the Web tab, you should see your link at the 'Configuration for <website_name>'. In our case it is 'syarifh.pythonanywhere.com'.
Click the link to visit your website.

![Screenshot 2024-01-17 013336](https://github.com/FirdausHakimii/Group-7/assets/148948107/66ce9471-4e5b-49d2-a4ff-9a97774a83d9)

