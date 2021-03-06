from flask import Flask, request

app = Flask(__name__)

#these are GET functions
@app.route("/")
def hello_world():
    return "<p>This is a test for Lesson 2!</p>"

#GET function
@app.route("/about/")
def about():
    return "<p>About the use of flask</p>"

#GET function
@app.route("/square/<number>")
def square(number):
    n = number**number
    return "<p>" + str(n) + "</p>"
    #return "<p>The square of number is" + str(n) + "</p>"


    #Post function
@app.route("/users", methods=['POST'])
def users():
    data = request.form
    first_name = data["first_name"]
    last_name = data["last_name"]
    return "<p>new_user_added" + first_name + last_name + "</p>"