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

@app.route('/books',methods= ['GET'])
@jwt_required
def getBooks():
    bookController = BookController()
    return jsonify(bookController.getBooks())

@app.route('/books/<int:book_id>',methods= ['GET'])
@jwt_required
def getBookById(book_id):
    bookController = BookController()
    return jsonify(bookController.getBookById(book_id))

@app.route('/books/<int:book_id>',methods= ['PUT'])
@jwt_required
def updateBookNameById(book_id):
    bookname = request.form.get('name', None)
    bookController = BookController()
    if bookname is None:
        return jsonify({"error": "check your input"}), 403
    return jsonify(bookController.updateBook(book_id,bookname))

@app.route('/books/<int:book_id>',methods= ['DELETE'])
@jwt_required
def deleteBookNameById(book_id):
    bookController = BookController()
    return jsonify(bookController.deleteBook(book_id))

#TODO function for handling errors such 404, wrong method invocation

if __name__ == '__main__':
    app.run()

