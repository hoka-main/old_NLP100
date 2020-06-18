import sys

args = sys.argv
print(args)

with open(args[1]) as col1, \
        open(args[2]) as col2,\
        open('cols.txt', mode='w') as write_cols:

    for line1, line2 in zip(col1, col2):
        col1_split = line1.split('\n')
        col2_split = line2.split('\n')
        write_cols.write(col1_split[0] + '\t' + col2_split[0] + '\n')

