import shutil


def mo():
    with open('file_name.txt') as fn:
        ch = fn.read()
        file_name = []
        file_path = []
        name = []
        file_list = ch.split('.pdf')
        count = 0
        for fp in file_list:
            fp = fp.lstrip()
            fp = fp + '.pdf'
            if fp != '\n.pdf':
                file_path.append(fp)
                n = fp.split('/')
                for nm in n:
                    if nm[-4:] == '.pdf':
                        if nm == '.pdf':
                            nm = str(count) + nm
                            count += 1
                        name.append(nm)


def move(path):
    for path in file_path:
        shutil.move(path, './pdfs')


def main():
    with open('file_path.txt') as path:
        name = []
        path = path.readlines()
        for i in path:
            i = i[:-1]
            l = i.split('/')
            for n in l:
                if n[-4:] == '.pdf':
                    name.append(n)
    print(len(name))
    print(len(path))
    move(path)


if __name__ == '__main__':
    main()

# for f in path_list:
#     f = 'pdfs/' + f
#     with open()
