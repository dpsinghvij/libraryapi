from sqlalchemy import Integer, Column, NVARCHAR, func, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from sqlalchemy import create_engine
Base= declarative_base()

secret_key= "121211"

class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key= True)
    name = Column(NVARCHAR(100), nullable= False)
    email = Column(NVARCHAR(100), nullable= False)
    password = Column(EncryptedType(NVARCHAR(100), secret_key, AesEngine, 'pkcs5'))
    created_dt = Column(DateTime, default=func.now())

class Book(Base):
    __tablename__= "books"
    id = Column(Integer, primary_key=True)
    name = Column(NVARCHAR(100), nullable=False)
    author= Column(NVARCHAR(100),nullable= False)
    created_dt = Column(DateTime, default=func.now())
    uploader_id= Column(Integer, ForeignKey('user.id'))

engine= create_engine('mysql+pymysql://libadmin:library@localhost/library?charset=utf8')
try:
    Base.metadata.create_all(engine)
    print("Tables created")
except Exception as error:
    print(error)