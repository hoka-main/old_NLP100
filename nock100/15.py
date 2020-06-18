import sys
# import linecache
# 今回は使わない

args = sys.argv

print(args)
print('第1引数:' + args[1])
print('第2引数:' + args[2])
intN = int(args[1])

list_box = []
with open(args[2]) as names:
    for re_line in names:
        list_box.insert(0, re_line)
    for line, N in zip(list_box, range(intN)):
        if N < 0:
            break
        else:
            print(line)
            N -= 1

    # target_line = linecache.getline(names, int(intN))
    # print(target_line)
    # linecache.clearcache()
    # なぜか動かないし使わない。
