import sys

args = sys.argv

print(args)

print('第1引数:' + args[1])
intN = int(args[1])
with open('cols.txt', mode='r') as names:
    for line, N in zip(names, range(intN)):
        if N < 0:
            break
        else:
            print(line)
            N -= 1


