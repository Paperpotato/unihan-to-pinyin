#! /usr/bin/env python3

import json
from ntpath import join

data_file = 'hanzi_to_jyutping.json'

file_handler = open(data_file, 'r')
mappings = json.load(file_handler)

input_file = 'input.txt'
input_file_handler = open(input_file, 'r')
input_raw = input_file_handler.read().split('\n')

processed_text = ''

# for c in input_raw:
#     print(c.split('\t')[0])
    
#     split_line = c.split('\t')
#     characters_to_convert = [char for char in split_line[0]]
#     try:
#         result = ''
#         for char in characters_to_convert:
#             split_words = mappings[char].split(' ')
#             if len(split_words) > 1:
#                 result = mappings[char]
#             else:
#                 result += f'{mappings[char]} '

#     except KeyError as keyerr:
#         result = ''
#     finally:
#         split_line[0] = split_line[0] + f': {result}'
#         c = '\t'.join(split_line)
#         with open('output.txt', 'a') as f:
#             f.write(c)
#             f.write('\n')
#         print(c)

for c in input_raw:
    split_line = c.split(':')
    
    split_line[1] = split_line[1] + ' ' + split_line[2]
    joined_line = split_line[0] + ': ' + split_line[1]
    print(joined_line)

    with open('output.txt', 'a') as f:
        f.write(joined_line)
        f.write('\n')
    # print(c)

