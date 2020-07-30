import sys
from collections import Counter
import json

args = sys.argv

list_out = []

with open(args[1], mode='r') as from_file, \
        open(args[2], mode='w') as to_file, \
        open(args[3], mode='w') as up_sort, \
        open(args[4], mode='w') as count_sort:
    for line in from_file:
        line = line.replace(',', '')
        line = line.replace('!', '')
        line = line.replace('.', '')
        line = line.replace('?', '')
        line = line.replace('\t', ' ')
        line = line.replace('[', '')
        line = line.replace(']', '')
        line = line.replace('(', '')
        line = line.replace(')', '')
        line2 = line
        to_file.write(line)
        line2 = line2.replace('\n', ' ')
        object100 = line2.split()
        for obj in object100:
            list_out.append(obj)
    counter_dict = Counter(list_out)
    text = json.dumps(counter_dict)
    count_sort.write(text)
    counter_dict = Counter(list_out)
    sorted_dict = sorted(counter_dict.items())
    text = json.dumps(sorted_dict)
    up_sort.write(text)



