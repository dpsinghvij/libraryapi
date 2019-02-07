from controller.Controller import Controller
from models.dbmodels import User, Book


class BookController(Controller):

    def addBook(self, name, author, uploader_email):
        #create session
        self.create_session()
        #get user id
        user = self.session.query(User).filter(User.email == uploader_email).first()
        userid= user.id
        #create a book object
        book= Book(name=name,author=author,uploader_id=userid)
        #save book object
        try:
            self.session.add(book)
            self.session.commit()
            return book.toDict()
        except Exception as exception:
            return {"error":"error while inserting records "+str(exception)}
        finally:
            # end_session
            self.end_session()



    def getBooks(self):
        self.create_session()
        books=self.session.query(Book).all()
        self.end_session()
        return [book.toDict() for book in books]

