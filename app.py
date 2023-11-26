
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
               if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]
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


@app.route('/cart')
def view_cart():
    # Retrieve the indices of books in the cart from the session
    cart_indices = session.get('cart', [])

    # Create a list of unique books in the cart with their quantities
    cart = [{'book': catalog[index], 'quantity': cart_indices.count(index)} for index in set(cart_indices)]

    # Calculate the total price of items in the cart
    total_price = sum(item['book']['price'] * item['quantity'] for item in cart)
    return render_template('cart.html', cart=cart, total_price=round(total_price,2))


#_______________________________________________________________

# Add a route for clearing the cart
@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
#_______________________________________________________________________________________________


