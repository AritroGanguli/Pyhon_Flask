from flask import Flask
import random
## quotes = [
##                "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
##                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
##                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
##                "Listen to many, speak to a few.",
##                "Only when the tide goes out do you discover who has been swimming naked."
##    ]
## Define a flask application name 'app' below
## Define a view function 'hello', which displays the message
## "Hello World!!! I've run my first Flask application."
## The view function 'hello' should be mapped to URL '/'.
## Define a view function 'hello_user', which takes 'username' as an argument
## and returns the html string containing a 'h2' header  "Hello <username>"
## After displaying the hello message, the html string must also display one quote,
## randomly chosen from the provided list `quotes`
## Before displaying the quote, the html string must contain the 'h3' header 'Quote of the Day for You'
## The view function 'hello_user' should be mapped to URL '/hello/<username>/' .
## Use the list 'quotes' in 'hello_user'  function
## Define a view function 'display_quotes', which returns an html string
## that displays all the quotes present in 'quotes' list in a unordered list.
## Before displaying 'quotes' as an unordered list, the html string must also include a 'h1' header "Famous Quotes".
## The view function 'display_quotes' should be mapped to URL '/quotes/' .
## Use the below list 'quotes' in 'display_quotes'  function
## Write the required code which runs flask applictaion 'app' defined above
## on host 0.0.0.0 and port 8000

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!!! I've run my first Flask application."


@app.route("/hello/<username>/")
def hello_user(username):
  quotes = [
  "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
  "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
  "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
  "Listen to many, speak to a few.",
  "Only when the tide goes out do you discover who has been swimming naked."
  ]
  return "<h2>Hello " + username + "</h2>" + "<h3>Quote of the Day for You</h3>" + random.choice(quotes)


@app.route("/quotes/")
def display_quotes():
  quotes = [
  "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
  "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
  "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
  "Listen to many, speak to a few.",
  "Only when the tide goes out do you discover who has been swimming naked."
  ]
  return "<h1>Famous Quotes</h1><ul><li>" + quotes[0] + "</li><li>" + quotes[1] + "</li><li>" + quotes[2] + "</li><li>" + quotes[3] + "</li><li>" + quotes[4] + "</li></ul>"

if __name__ == '__main__':
  app.run('0.0.0.0', 8000)