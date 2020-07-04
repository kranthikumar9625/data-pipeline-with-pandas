#thois is for reading the data
import sqlalchemy
from util import get_connection

def read_table(db_details, table_name, limit=0):
    SOURCE_DB = db_details['SOURCE_DB']

    connection = get_connection(
        db_type = SOURCE_DB['DB_TYPE'],
        db_host = SOURCE_DB['DB_HOST'],
        db_port = SOURCE_DB['DB_PORT'],
        db_name = SOURCE_DB['DB_NAME'],
        db_user = SOURCE_DB['DB_USER'],
        db_pass = SOURCE_DB['DB_PASS']
    )
    print('read query building')
    if limit == 0:
        query = sqlalchemy.text(f'select * from {table_name}')
    else:
        query = sqlalchemy.text(f'select * from {table_name} limit {limit}')
    result =  connection.execute(query).fetchall()
    print("data fetched")
    column_names = result[0].keys()

    # connection.dispose()

    return result,column_names
