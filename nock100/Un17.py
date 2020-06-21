import sys


def split_by_column(file, split, indent):
    result = []
    for line in file:
        list_box = line.split(split)
        result.append(list_box[indent])
    return result


args = sys.argv
no_list = []
names_list = []
with open(args[1]) as names:
    names_list = split_by_column(names, '\t', 2)
    for variable in names_list:
        print(variable)
        no_list.append(variable)
# no_list.sort()
# print(no_list)
