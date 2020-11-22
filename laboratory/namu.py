import re


def main():
    s = 'namuamidabutu.txt'
    string = ''
    with open(s, mode='r') as nam:
        nam = nam.readlines()
        for line in nam:
            line = line.replace('\n', '')
            line = line.replace('。', '')
            line = line.replace('、', '')
            line = line.replace(' ', '')
            line = line.replace('　', '')
            line = line.replace('?', '')
            string = string + line
        print(string)


if __name__ == '__main__':
    main()