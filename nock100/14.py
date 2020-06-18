import sys

args = sys.argv

print(args)

print('第1引数:' + args[1])
intN = args[1]
with open('popular_names.txt', mode='w') as names:
    for line in names:
        cols = line.split('\t')

