import sys


def make_line_list(file, split):
    result = []
    for line in file:
        r_strip_line = line.rstrip('\n')
        list_in_list = r_strip_line.split(split)
        num_box3 = list_in_list.pop()
        num_box2 = list_in_list.pop()
        list_in_list.append(int(num_box2))
        list_in_list.append(int(num_box3))
        result.append(list_in_list)
    return result


args = sys.argv
args.insert(1, 'popular-names.txt')
no_list = []
name_list = []
with open(args[1]) as names:
    name_list = make_line_list(names, '\t')
    set_variable = set()
    for variable in name_list:
        set_variable.add(variable[2])
    print(set_variable)
# no_list.sort()
# print(no_list)
