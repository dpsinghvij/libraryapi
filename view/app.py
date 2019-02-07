import json

from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity

from controller.BookController import BookController
from controller.UserController import UserController

app= Flask("libraryapp")
app.config['JWT_SECRET_KEY'] = 'JWTKEY'
jwt = JWTManager(app)

@app.route('/')
def index():
    return "Welcome to the Library"

@app.route('/registration', methods= ['POST'])
def registration():
    name= request.form.get('name', None)
    email= request.form.get('email', None)
    password= request.form.get('password', None)
    message = []
    if name is None or email is None or password is None:
        return jsonify({"error":"check your input"}),403
    userController= UserController()
    return jsonify(userController.registerUser(name=name,email=email,password=password))

@app.route('/login', methods= ['POST'])
def login():
    email= request.form.get('email', None)
    password= request.form.get('password', None)
    message = []
    if email is None or password is None:
        return jsonify({"error": "check your input"}), 403
    userController = UserController()
    return jsonify(userController.loginUser(email=email, password=password))


@app.route('/books',methods= ['POST'])
@jwt_required
def addBook():
    user_email= get_jwt_identity()
    author = request.form.get('author', None)
    bookname = request.form.get('book_name', None)
    if author is None or bookname is None:
        return jsonify({"error": "check your input"}), 403
    bookController= BookController()
    return jsonify(bookController.addBook(name=bookname,author=author,uploader_email=user_email))


if __name__ == '__main__':
    app.run()

