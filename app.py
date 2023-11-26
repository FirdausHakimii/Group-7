
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure random key


catalog = [
    {'title': 'Kaiju No.8', 'author': 'Naoya Matsumoto', 'genre': 'Fiction', 'price': 19.99, 'cover_image': 'book_cover (1).jpg'},
    {'title': 'Spy X Family', 'author': 'Tatsuya Endo', 'genre': 'Fiction', 'price': 29.99, 'cover_image': 'book_cover (2).jpg'},
    {'title': 'The Hobbit', 'author': 'J. R. R. Tolkien', 'genre': 'Fiction', 'price': 19.99, 'cover_image': 'book_cover (3).jpg'},
    {'title': 'Throne of Glass', 'author': 'Sarah J. Maas', 'genre': 'Fiction', 'price': 19.99, 'cover_image': 'book_cover (4).jpg'},
    {'title': 'Harry Potter', 'author': 'J. K. Rowling', 'genre': 'Fiction', 'price': 19.99, 'cover_image': 'book_cover (5).jpg'},
    # Add more books as needed
]


@app.route('/')
def home():
    return render_template('index.html', catalog=catalog)
    
