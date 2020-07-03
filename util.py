import pandas as pd
from config import DB_DETAILS
import sqlalchemy
import pymysql
import psycopg2


def get_tables(path):
    tables = pd.read_csv(path, sep = ':')
    return tables.query("to_be_loaded == 'yes'")

def load_db_details(env):
    return DB_DETAILS(env)

def get_mysql_connection(db_host,db_port,db_name,db_user,db_pass):
    try:
        connection = sqlalchemy.create_engine(f"mysql+pymysql://%s:%s@%s:%s/%s" \
                                              % (db_user, db_pass, db_host, db_port, db_name))
        print("connection to mysql database is succesfull")
        return connection
    except sqlalchemy.exc.SQLAlchemyError as e:
        print(type(e))

def get_postgresql_coinnection(db_host,db_port,db_name,db_user,db_pass):
    try:
        connection = sqlalchemy.create_engine(f"postgresql+psycopg2://%s:%s@%s:%s/%s" \
                                              % (db_user, db_pass, db_host, db_port, db_name))
        print("connection to postgresql database is succesfull")
        return connection
    except sqlalchemy.exc.SQLAlchemyError as e:
        print(type(e))


def get_connection(db_type,db_host,db_port,db_name,db_user,db_pass):
    connection = None
    if db_type == 'mysql':
        connection = get_mysql_connection(db_host,db_port,db_name,db_user,db_pass)
        return connection
    if db_type == 'postgresql':
        connection = get_mysql_connection(db_host, db_port, db_name, db_user, db_pass)
        return connection

