from sqlalchemy.orm import sessionmaker

from models.dbmodels import engine


class Controller():
    def create_session(self):
        Session= sessionmaker(bind= engine)
        self.session= Session()

    def end_session(self):
        self.session.close()