import sys
import collections
from package import func


def to_split_row(file, split, indent):
    to_split_list = []
    for line in file:
        list_box = line.split(split)
        to_split_list.append(list_box[indent])
    return to_split_list


args = sys.argv
args.append('ch02/popular-names.txt')

with open(args[1]) as names:
    name_list = to_split_row(names, '\t', 0)
    counted_names_dict = collections.Counter(name_list)
    print(counted_names_dict)
