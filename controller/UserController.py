from flask_jwt_extended import create_access_token

from controller.Controller import Controller
from models.dbmodels import User


class UserController(Controller):

    def registerUser(self, name, email, password):
        # initialize a session
        self.create_session()
        # query database to check if user is already there
        user= self.session.query(User).filter_by(email=email).first()
        # if user is already there, then send a message that user is already there
        if user is not None:
            return {"error": "Email already exists"}
        # if user is not already present then create a user
        try:
            user= User(name=name,email=email,password=password)
            self.session.add(user)
            self.session.commit()
            self.end_session()
            # use email id to create JWT token
            token= create_access_token(identity=email)
            # return the user info with the token
            return {"accesstoken": token}
        except Exception as exception:
            return {"error" : "error in inserting record "+ str(exception)}
