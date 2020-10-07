import csv
import sys
import os


def main():
    args = sys.argv
    args.append('program_.csv')

    with open(args[1], newline='') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            line = ', '.join(line)
            line = line.replace(')-', ')')
            line = line.replace(', ', '-')
            line = line.replace('/', ':')
            os.makedirs(line)


if __name__ == '__main__':
    main()
