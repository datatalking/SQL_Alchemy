# SOURCE Essential_SQLAlchemy_2nd_Edition.pdf
# SOURCE https://docs.sqlalchemy.org/en/13/orm/tutorial.html#version-check
# SOURCE https://medium.com/swlh/orm-and-sqlalchemy-the-magic-wand-in-database-management-a2d02877a57a
# TODO https://alembic.sqlalchemy.org/en/latest/front.html
# FILENAME Chapter1
# INFO since sql is at the core of all data I need to be a data guru,
# thus a SQL guru is needed skill
# TODO find sqlalchemy.__version__ testing options, pytest?
# https://stackoverflow.com/questions/23325669/writting-py-test-for-sqlalchemy-app
# TODO https://stackoverflow.com/questions/58660378/how-use-pytest-to-unit-test-sqlalchemy-orm-classes

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import json
from sqlalchemy.dialects.sqlite import json
from sqlalchemy.dialects.mysql import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence

Base = declarative_base()


def main():
    create_test_mysql_dbase()
    # TODO find a way to test sqlalchemy.__version__ = version we need


class User(Base):
    """
    a base class to catalog of user classes and tables
    """
    __tablename__ = 'users'
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))  # TODO vs uuid
    fullname = Column(String(50))  # TODO vs uuid
    nickname = Column(String(50))  # TODO vs uuid
    
    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}')>"
        # converted to f string vs in book example was verbose
    


def create_test_sqlite_dbase():
    engine = create_engine('sqlite:///:memory:', echo = True)
    # echo True enables logging of generated sql


def create_test_postgresql_dbase():
    postgresql_engine = create_engine('postgresql+psycopg2://username:password@localhost:' \
                           '5432/mydb')
    connection = postgresql_engine.connect()
    # TODO test pool_recycle (assert !=-1) etc which is default for no timeout vs 3600
    # TODO test echo is xyz
    # TODO test encoding is xyz
    # TODO test isolation_level is xyz
    
    
def create_test_mysql_dbase():
    mysql_engine = create_engine('mysql+pymsql://cookiemonster:chocolatechip'
                           '@mysql01.monster.internal/cookies', pool_recyle=3600)
    connection = mysql_engine.connect()
    # TODO test pool_recycle (assert !=-1) etc which is default for no timeout vs 3600
    # TODO test echo is xyz
    # TODO test encoding is xyz
    # TODO test isolation_level is xyz
