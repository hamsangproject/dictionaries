import sqlite3
import json
from sqlite3.dbapi2 import connect
from sys import argv
import os

sql_filename = 'dics.db'

connection = sqlite3.connect(sql_filename)

# get filenames from shell and add them as tables into database
for json_filename in argv[1:]:
    table_name = os.path.basename(json_filename)[:-5]

    # create table
    connection.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                    (id INTEGER, word TEXT, definition TEXT, context TEXT)''')
    
    json_file = open(json_filename)
    json_db = json.load(json_file, strict=False)
    for id, entry in enumerate(json_db):
        connection.execute(f'INSERT INTO {table_name} VALUES (?, ?, ?, ?)', (id, entry['word'], entry['definition'], entry['context']))

    connection.commit()    


