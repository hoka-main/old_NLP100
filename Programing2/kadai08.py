import sys
args = sys.argv

args[1]
args[2]

with open(args[1], mode='r') as from_file, \
        open(args[2], mode='w') as to_file:
    for line in from_file:
        to_file.write(line)

