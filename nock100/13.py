import sys

args = sys.argv

import_file_col1 = 'col1.txt'
import_file_col2 = 'col2.txt'


with open('col1.txt', mode='r') as col1, \
        open('col2.txt', mode='r') as col2,\
        open('cols.txt', mode='w') as write_cols:

    for line1, line2 in zip(col1, col2):

        col1_split = line1.split('\n')
        col2_split = line2.split('\n')
        write_cols.write(col1_split[0] + '\t' + col2_split[0] + '\n')

