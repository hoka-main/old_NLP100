import sys
from package import func
args = sys.argv
args.insert(1, '5')
args.insert(1, 'cols.txt')

print(args)
intN = int(args[2])
with open(args[1]) as names:
    line_count = func.count(names)
    division = line_count // intN

    for line, N in zip(names, range(division)):
        if N < 0:
            break
        else:
            print(line)
            N -= 1

