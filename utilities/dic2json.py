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

    if line == '*\n':
        entry['definition'] = entry['definition'][:-1]
        database.append(entry)
        entry = {'word': '',
                 'definition': '',
                 'context': '',
                 }

        mode = 0
    
    elif mode == 0:
        entry['word'] = line[:-1]
        mode = 2

    elif mode == 2:
        if re.match(r'\[.*\] \n', line) is not None:
            entry['context'] = line [1:-3]
        else:
            entry['definition'] += line

outfile = open(json_filename, 'w')
json_str = json.dumps(database, ensure_ascii=False, indent=1)
json_str_clean = json_str.replace('\\n', '\n')
outfile.write(json_str_clean)