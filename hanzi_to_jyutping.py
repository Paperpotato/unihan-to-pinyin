#! /usr/bin/env python3

import json

data_file = 'hanzi_to_jyutping.json'

file_handler = open(data_file, 'r')
mappings = json.load(file_handler)

input_file = 'Business Chinese.txt'
input_file_handler = open(input_file, 'r')
input_raw = input_file_handler.read().split('\n')

processed_text = ''

for c in input_raw:
    split_line = c.split('\t')
    for i, char in enumerate(split_line):
        split_line[i] = char.replace('&nbsp;', '')
    try:
        result = ''
        for char in split_line[1]:
            split_words = mappings[char].split(' ')
            if len(split_words) > 1:
                result = mappings[char]
            else:
                result += f'{mappings[char]} '

    except KeyError as keyerr:
        result = ''
    finally:
        split_line[4] = split_line[4] + f': {result}'
        c = '\t'.join(split_line)
        with open('output.txt', 'a') as f:
            f.write(c)
            f.write('\n')
        print(c)

