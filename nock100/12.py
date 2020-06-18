import sys

args = sys.argv
print(args)

with open(args[1]) as import_date,  \
        open('col1.txt', mode='w') as col1_file, \
        open('col2.txt', mode='w') as col2_file:

    for line in import_date:
        cols = line.split('\t')
        col1_file.write(cols[0] + '\n')
        col2_file.write(cols[1] + '\n')

