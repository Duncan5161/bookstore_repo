from flask import Flask, render_template, request, redirect 
from database_connection import *
from lib.book_repository import *
from lib.user_repository import *

# instantiate a Flask app object
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

@app.route("/", methods=["GET"])
def index():
    
    return render_template("index.html")

@app.route('/books', methods=['GET'])
def books():
    connection = DatabaseConnection()
    connection.connect()
    book_repository=BookRepository(connection)
    books = book_repository.all()
    return render_template("books.html", books=books)

@app.route('/books', methods=['POST'])
def create_book():
    
    connection = DatabaseConnection()
    connection.connect()
    book_repository=BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repository.create(book)
    return redirect("/books")

@app.route('/users/new', methods=['GET'])
def get_signup_form():
    return render_template("signup_form.html")

@app.route('/users', methods=['POST'])
def create_user():
    
    connection = DatabaseConnection()
    connection.connect()
    user_repository=UserRepository(connection)
    user_details = request.form
    print(user_details)
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect("/thank_you")

@app.route('/thank_you', methods=['GET'])
def thank_you():
    return render_template("thank_you.html")

@app.route("/films", methods=['GET'])
def films():
     
    connection = DatabaseConnection()
    connection.connect()
    films_dict = connection.execute('SELECT * FROM films')
    films = [{"film": film["film"], "release_year": film["release_year"]} for film in films_dict]
    return render_template("films.html", films=films)

@app.route('/authors', methods =['GET'])
def authors():
        author_list = [
                        {
                            "name": "Julia Donaldson",
                            "dob": "1948-09-16"
                        },
                        {
                            "name": "Andrea Beaty",
                            "dob": "1961-10-08"
                        },
                        {
                            "name": "Kelly Barnhill",
                            "dob": "1973-01-01"
                        },
                        {
                            "name": "Zetta Elliott",
                            "dob": "1979-11-11"
                        }
                        ]
        return author_list

@app.route("/book_list", methods=["GET"])
def book_list():
    
    return render_template("book_list.html")

@app.route("/quotes", methods=['GET'])
def quotes():
     
     return(render_template("quotes.html"))

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
    
