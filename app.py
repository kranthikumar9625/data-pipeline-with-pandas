#
import sys
from config import DB_DETAILS
from util import get_tables
from read_file import read_table

def main():
    """ this takes atleast one argiument"""

    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    tables = get_tables('table_list')
    for table in tables['table_name']:
        data,column_names = read_table(db_details,table,limit=10)
        for rec in data:
            print(rec)



if __name__ == '__main__':
    main()
