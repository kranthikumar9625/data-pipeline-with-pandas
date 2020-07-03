#
import sys
from config import DB_DETAILS

def main():
    """ this takes atleast one argiument"""

    env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)

if __name__ == '__main__':
    main()
