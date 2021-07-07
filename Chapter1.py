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


# TODO oracle paintstone uses 7818 mc free forever


from sqlalchemy import (Column, create_engine, DateTime, ForeignKey, Integer, MetaData, Numeric, Sequence, String, Table)
from sqlalchemy.dialects.postgresql import json
from sqlalchemy.dialects.sqlite import json
from sqlalchemy.dialects.mysql import json
from datetime import datetime

metadata = MetaData()

def main():
    create_test_mysql_dbase()
    # TODO find a way to test sqlalchemy.__version__ = version we need
    create_cookie_dbase()
    create_users_dbase()
    

def create_test_sqlite_dbase():
    engine = create_engine('sqlite:///:memory:', echo=True)
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


def create_cookie_dbase(cookie_id, cookie_name, cookie_recipe_url, cookie_sku, quantity, unit_cost):
    cookies = Table('cookies', metadata,
                    Column('cookie_id', Integer(), primary_key=True),
                    Column('cookie_name', String(50), index=True),
                    Column('cookie_recipe_url', String(255)),
                    Column('cookie_sku', String(55)),
                    Column('quantity', Integer()),
                    Column('unit_cost', Numeric(12, 2))
                    )


def create_users_dbase(user_id, username, email_address, phone, password, created_on, updated_on):
    """constrints on String will enable Oracle cx_oracle use"""
    from sqlalchemy import MetaData
    metadata = MetaData
    users = Table('users', metadata,
                  Column('user_id', Integer(), primary_key=True),
                  Column('username', String(15), nullable=False, unique=True),
                  Column('email_address', String(255), nullable=False),
                  Column('phone', String(20), nullable=False),
                  Column('password', String(25), nullable=False),
                  Column('created_on', DateTime(), default=datetime.now),
                  Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
                  )


def create_orders_dbase(orders, order_id, user_id):
    orders = Table('orders', metadata,
                   Column('order_id', Integer(), primary_key=True),
                   Column('user_id', ForeignKey('users.user_id'))
                   )


def create_line_item_dbase(line_items, line_items_id, order_id, cookie_id, quantity, extended_cost):
    line_items = Table('line_items', metadata,
                       Column('line_items_id', Integer(), primary_key=True),
                       Column('order_id', ForeignKey('orders.order_id')),
                       Column('cookie_id', ForeignKey('cookies.cookie_id')),
                       Column('quantity', Integer()),
                       Column('extended_cost', Numeric(12, 2))
                       )

engine = create_engine('sqlite:///:memory:')
metadata.create_all(engine)



# Keys and Constraints
"""Keys and constraints ensure data requirements, uniquness, primacy, non zero, non negative etc"""
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint

PrimaryKeyConstraint('user_id', name='user_pk')

UniqueConstraint('username', name='uix_username')

