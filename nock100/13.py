import_file_col1 = 'col1.txt'
import_file_col2 = 'col2.txt'


with open(import_file_col1) as col1, \
        open(import_file_col2) as col2,\
        open('cols.txt', mode='w') as write_cols:

    for line1 in col1:
        line1.replace('\n', '')
        for line2 in col2:
            write_cols.write(line1 + '\t' + line2)

