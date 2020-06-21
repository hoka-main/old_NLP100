import sys
from package import func
args = sys.argv

print(args)
intN = int(args[2])
with open(args[1]) as count_names, \
        open(args[1]) as names:
    line_count = func.count(count_names)
    quotient = line_count // intN
    func.print_line(zip(names, range(quotient)))
