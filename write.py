#writing the data to db
from util import get_connection
import sqlalchemy

def build_query(table_name,column_names):
    column_values = tuple(map(lambda column:column.replace(column,'%s')))
    query = sqlalchemy.text(f'Insert INTO {table_name} {column_names} VALUES {column_values}')
    return query
