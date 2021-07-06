from sqlalchemy import create_engine

def main():
    create_test_mysql_dbase()


def create_test_postgresql_dbase():
    engine = create_engine('postgresql+psycopg2://username:password@localhost:' \
                           '5432/mydb')
    connection = engine.connect()
    # TODO test pool_recycle (assert !=-1) etc which is default for no timeout vs 3600
    # TODO test echo is xyz
    # TODO test encoding is xyz
    # TODO test isolation_level is xyz
    
def create_test_mysql_dbase():
    engine = create_engine('mysql+pymsql://cookiemonster:chocolatechip'
                           '@mysql01.monster.internal/cookies', pool_recyle=3600)
    # TODO test pool_recycle (assert !=-1) etc which is default for no timeout vs 3600
    # TODO test echo is xyz
    # TODO test encoding is xyz
    # TODO test isolation_level is xyz
    
