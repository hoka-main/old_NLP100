import sys

args = sys.argv
print(args)
intN = int(args[1])

with open('cols.txt', mode='r') as names:

    for line, N in zip(names, range(intN)):
        if N < 0:
            break
        else:
            print(line)
            N -= 1


