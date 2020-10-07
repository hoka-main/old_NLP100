import sys
import pprint
from package import func

args = sys.argv
args.insert(1, 'ch02/popular-names.txt')

with open(args[1]) as file:
    name_list = func.make_line_list(file, '\t')
    print(name_list)
    name_list.sort(key=lambda x: x[2], reverse=True)
    pprint.pprint(name_list, width=40)
