import json
import re
from sys import argv
import os

# get .dic filename from shell
dic_filename = argv[1]

# file to write output into
json_filename = os.path.basename(dic_filename)
if json_filename.endswith('.dic'):
    json_filename = json_filename[:-4]
json_filename += '.json'

dicfile = open(dic_filename)

# a dictionary containing everything about a word
# word, definition, context
entry = {'word': '',
         'definition': '',
         'context': '',
         }

# a list containing all words. each element is a dictionary
database = []

mode = 0
for line in dicfile:

    entry['word'] = line[:-1]
    database.append(entry)

    entry = {'word': '',
            'definition': '',
            'context': '',
            }


outfile = open(json_filename, 'w')
json_str = json.dumps(database, ensure_ascii=False, indent=1)
json_str_clean = json_str.replace('\\n', '\n')
outfile.write(json_str_clean)
