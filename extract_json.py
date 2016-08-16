#
#   @author      : SRvSaha
#   Filename     : extract_json.py
#   Timestamp    : 12:02 15-August-2016 (Monday)
#   Description  : Extracts the required values from JSON format
#
import json
import sys

filename = sys.argv[1]

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    output_file  = ""
    json_to_dict = json.loads(line)
    output_file = str(json_to_dict['id']) + ".txt"
    text = json_to_dict['text']

    with open(output_file,'w') as f:
        f.write(text)
