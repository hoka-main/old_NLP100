import sys


def print_line(zip_type):
    for line, N in zip_type:
        if N < 0:
            break
        else:
            print(line)
            N -= 1


args = sys.argv
print(args)
intN = int(args[1])

with open('cols.txt', mode='r') as names:
    print_line(zip(names, range(intN)))



