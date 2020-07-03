#db details

import os

DB_DETAILS = {
    'dev' : {
        'SOURCE_DB' : {
            'DB_TYPE' : 'mysql',
            'DB_HOST' : 'localhost',
            'DB_NAME' : 'retail_db',
            'DB_USER' : os.environ.get('source_db_user'),
            'DB_PASS' : os.environ.get('source_db_pass')

        },
        'TARGET_DB' : {
            'DB_TYPE' : 'mysql',
            'DB_HOST' : 'localhost',
            'DB_NAME' : 'retail_db',
            'DB_USER' : os.environ.get('target_db_user'),
            'DB_PASS' : os.environ.get('target_db_pass')

        }
    }
}