# Group 7
# Group members:
# 1. Muhammad Firdaus Hakimi
# 2. Abdullah Aiman bin Jaafar - B21MJ0001
# 3. Syarif Hidayatullah bin Muhmmad Nasir - A21MM0093


from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy                                            #added line

#app = Flask(__name__)
#app.secret_key = 'your_secret_key'  # Change this to a secure random key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use SQLite for simplicity
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure random key
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    balance = db.Column(db.Float, default=100.0)  # Virtual balance, starting with $100 #############

# Database creation and initialization
with app.app_context():    
    db.create_all()


catalog = [
    {'title': 'Kaiju No.8', 'author': 'Naoya Matsumoto', 'genre': 'Fiction', 'price': 19.99, 'cover_image': 'book_cover (1).jpg'},
    {'title': 'Spy X Family', 'author': 'Tatsuya Endo', 'genre': 'Fiction', 'price': 29.99, 'cover_image': 'book_cover (2).jpg'},
    {'title': 'The Hobbit', 'author': 'J. R. R. Tolkien', 'genre': 'Fiction', 'price': 19.99, 'cover_image': 'book_cover (3).jpg'},
    {'title': 'Throne of Glass', 'author': 'Sarah J. Maas', 'genre': 'Fiction', 'price': 19.99, 'cover_image': 'book_cover (4).jpg'},
    {'title': 'Harry Potter', 'author': 'J. K. Rowling', 'genre': 'Fiction', 'price': 19.99, 'cover_image': 'book_cover (5).jpg'},
    {'title': 'Python For Dummies', 'author': 'Stef Maruch', 'genre': 'Educational', 'price': 18.99, 'cover_image': 'book_cover (6).jpg'},
    {'title': 'If Animals Kissed Good Night', 'author': 'Ann Whitford Paul', 'genre': 'Kids', 'price': 4.19, 'cover_image': 'book_cover (7).jpg'},
    {'title': 'Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones', 'author': 'James Clear', 'genre': 'Self-Help', 'price': 13.79, 'cover_image': 'book_cover (8).jpg'},
    {'title': 'Rich Dad Poor Dad: What the Rich Teach Their Kids About Money That the Poor and Middle Class Do Not!', 'author': 'Robert T. Kiyosaki', 'genre': 'Finance', 'price': 18.99, 'cover_image': 'book_cover (9).jpg'},
    {'title': 'Physics for Scientists and Engineers: A Strategic Approach with Modern Physics', 'author': 'Randall Knight', 'genre': 'Educational', 'price': 51.99, 'cover_image': 'book_cover (10).jpg'},

    # Add more books as needed
]


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username is already taken
        if User.query.filter_by(username=username).first():
            return render_template('signup.html', error='Username is already taken.')

        # Create a new user and add it to the database
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Log in the new user
        session['username'] = username

        return redirect(url_for('home'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username and password match a registered user
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            # Log in the user
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Invalid username or password.')

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Clear the username from the session
    session.pop('username', None)
    return render_template('logout.html')

@app.route('/')
def home():
    return render_template('index.html', catalog=catalog)


@app.route('/search', methods=['POST'])
def search():

    # Retrieve the search query from the form
    query = request.form.get('query')

    # Filter books based on the query (case-insensitive)
    results = [{'title': book['title'],
                'author': book['author'],
                'genre': book['genre'],
                'price': book['price'],
                'cover_image': book['cover_image']} for book in catalog
               if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()or query.lower() in book['genre'].lower()]
    return render_template('search_results.html', results=results, catalog=catalog)

 
@app.route('/add_to_cart/<int:book_index>')
def add_to_cart(book_index):
    # Retrieve the existing cart from the session or initialize an empty list
    cart = session.get('cart', [])
    cart.append(book_index)

    # Update the session with the modified cart
    session['cart'] = cart

    print("Updated Cart Indices:", session['cart'])  # Add this line for debugging
    return redirect(url_for('home'))


@app.route('/cart')
def view_cart():
    # Retrieve the indices of books in the cart from the session
    cart_indices = session.get('cart', [])

    # Create a list of unique books in the cart with their quantities
    cart = [{'book': catalog[index], 'quantity': cart_indices.count(index)} for index in set(cart_indices)]

    # Calculate the total price of items in the cart
    total_price = sum(item['book']['price'] * item['quantity'] for item in cart)

    # Retrieve the current user                                                                            ####
    username = session.get('username')
    user = User.query.filter_by(username=username).first()
    
    # Fetch the user's balance                                                                       #####
    user_balance = user.balance

    # Display the total price of items in the cart and a link to the purchase page                     #####
    purchase_link = url_for('purchase')
    
    # return render_template('cart.html', cart=cart, total_price=round(total_price,2))
    # Add this line to get the correct link
    return render_template('cart.html', cart=cart, total_price=round(total_price, 2), purchase_link=purchase_link, user_balance=user_balance)

#_______________________________________________________________

# Add a route for clearing the cart
@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('home'))


@app.route('/purchase')                                                                                         ##################
def purchase():
    # Retrieve the indices of books in the cart from the session
    cart_indices = session.get('cart', [])

    # Create a list of unique books in the cart with their quantities
    cart = [{'book': catalog[index], 'quantity': cart_indices.count(index)} for index in set(cart_indices)]

    # Calculate the total price of items in the cart
    total_price = sum(item['book']['price'] * item['quantity'] for item in cart)

    # Retrieve the current user
    user = User.query.filter_by(username=session.get('username')).first()

    # Check if the user has enough balance to make the purchase
    if user.balance >= total_price:
        # Deduct the total price from the user's balance
        user.balance -= total_price

        # Update the session with the modified cart
        session['cart'] = []

        # Commit changes to the database
        db.session.commit()

        # Display a success message
        return render_template('purchase_success.html', total_price=round(total_price, 2))
    else:
        # Display an error message if the user does not have enough balance
        return render_template('purchase_error.html', total_price=round(total_price, 2))


if __name__ == '__main__':
    app.run(debug=True)
#_______________________________________________________________________________________________


