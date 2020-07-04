#
import sys
from config import DB_DETAILS
from util import get_tables
from read_file import read_table
from write import load_table
def main():
    """ this takes atleast one argiument"""

    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    tables = get_tables('table_list')
    print(tables)
    for table in tables['table_name']:
        print(table)
        data,column_names = read_table(db_details,table,limit=10)

        print(data)
        print(column_names)
        load_table(db_details,data,column_names,table)




if __name__ == '__main__':
    main()
