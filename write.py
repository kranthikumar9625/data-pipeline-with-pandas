#writing the data to db
from util import get_connection
import sqlalchemy

def build_query(table_name,column_names,rec):
    column_names_str = ', '.join(column_names)

    # column_values = tuple(map(lambda column:column.replace(column,'%s'),column_names))
    # print(column_values)
    # column_values_str = ', '.join(column_values)
    # print((column_values_str))
    query = sqlalchemy.text(f'INSERT INTO {table_name} ({column_names_str}) VALUES {rec}')
    print(query)
    return query


# def insert_data(connection,column_names,table_name,data,batch_size=1000):
#     query = 'table_name.insert()'
#     print(table_name)
#     recs = []
#     count = 1
#     for rec in data:
#         rec_dict = dict(zip(column_names,rec))
#         recs.append(rec_dict)
#         if count % batch_size == 0:
#             connection.execute(query,recs)
#             recs = []
#         count += 1
#     connection.execute(table_name.insert(), recs)
#     connection.dispose()

def insert_data(connection,data,table_name, column_names,batch_size=1000):

    #recs = []
    #count = 1
    for rec in data:
        #recs.append(rec)
        #if count % batch_size == 0:
        query = build_query(table_name,column_names,rec)
        print(query)
        connection.execute(query)
            #recs = []
        #count += 1
    #connection.execute(query, recs)
    connection.dispose()

def load_table(db_details, data, column_names, table_name):
    TARGET_DB = db_details['TARGET_DB']
    connection = get_connection(
        db_type=TARGET_DB['DB_TYPE'],
        db_host=TARGET_DB['DB_HOST'],
        db_port=TARGET_DB['DB_PORT'],
        db_name=TARGET_DB['DB_NAME'],
        db_user=TARGET_DB['DB_USER'],
        db_pass=TARGET_DB['DB_PASS']
    )
    #query = build_query(table_name, column_names)
    insert_data(connection, data,table_name, column_names)





