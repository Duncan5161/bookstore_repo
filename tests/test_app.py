import sys
import os 
from playwright.sync_api import Page, expect 

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import *

#0
def test_get_books_returns_200():
    client = app.test_client()

    response = client.get("/books")

    assert response.status_code == 200

#1
"""
If I send a GET request to books
200 status code is returned 
"""

def test_get_books_returns_all_the_books():

    client = app.test_client()
    response = client.get("/books")

    # here's where we assert that the response body contains all the books
    # note that we need to call .json on the response
    assert response.status_code == 200


#2
"""
When I send a GET request to the authors page
200 (success) status code a list of authors is returned in JSON formatting with a
"""

def test_authors_route_with_GET_request():
  
  client = app.test_client()
  response = client.get("/authors")

  assert response.json == [
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
  
  #3
  """
  If I send a request through the quote route
  a 200 (success) status code is returned 
  """

def test_quotes_returns_200_status_code():
     client = app.test_client()
     response = client.get("/quotes")
     assert response.status_code == 200

#4 
"""
If we send a GET request through the quotes route
All the quotes on the page are rendered as expected
"""
def test_has_quotes(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    page.goto("http://127.0.0.1:5001/quotes")
    ul = page.locator("ul > li")

    expect(ul).to_have_text(["I love writing stories that children can join in with. By Julia Donaldson",
    "Curiosity is the spark that drives discovery. By Andrea Beaty",
    "Stories are the way we make sense of the world. By Kelly Barnhill",
    "Books can be both mirrors and windows. By Zetta Elliott"])
    
    
#5
"""
If we send a GET request through the books route
All the books on the page are rendered as expected
"""
def test_has_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    page.goto("http://127.0.0.1:5001/book_list")
    book_list = page.locator("ul > li")

    expect(book_list).to_have_text(["The Gruffalo by Julia Donaldson",
    "Ada Twist, Scientist by Andrea Beaty",
    "The Girl Who Drank the Moon by Kelly Barnhill",
    "Dragons in a Bag by Zetta Elliott"])
  
#6
"""
If we send a POST request through the books route, adding a new book
The new book is added to the DB and rendered on the page as expected
"""
def test_add_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("title").fill("A Storm of Swords")
    page.get_by_placeholder("author").fill("George RR Martin")
    page.get_by_role("button", name="Submit").click()

    books = page.locator("p")
    new_book = books.all_inner_texts()[-1]
    assert new_book == "A Storm of Swords by George RR Martin"
  