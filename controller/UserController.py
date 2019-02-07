from _operator import and_

from flask_jwt_extended import create_access_token

from controller.Controller import Controller
from models.dbmodels import User


class UserController(Controller):

    def registerUser(self, name, email, password):
        # initialize a session
        self.create_session()
        # query database to check if user is already there
        user = self.session.query(User).filter(User.email==email).first()
        # if user is already there, then send a message that user is already there
        if user is not None:
            return {"error": "Email already exists"}
        # if user is not already present then create a user
        try:
            # NOTE: password should be encrypted and saved
            user = User(name=name, email=email, password=password)
            self.session.add(user)
            self.session.commit()

            # use email id to create JWT token
            token = create_access_token(identity=email)
            # return the user info with the token
            return {"accesstoken": token}
        except Exception as exception:
            return {"error": "error in inserting record " + str(exception)}
        finally:
            self.end_session()

    def loginUser(self, email, password):
        # initialize session
        self.create_session()
        # query database to query the user
        #NOTE: password should be encrypted and saved
        user = self.session.query(User).filter(and_(User.email == email, User.password == password)).first()
        # if user doesn't exist send an error message
        if user is None:
            return {"error": "email or password is incorrect"}
        # if the password is correct than return the accesstoken
        # use email id to create JWT token
        token = create_access_token(identity=user.email)
        # return the user info with the token
        self.end_session()
        return {"accesstoken": token}


