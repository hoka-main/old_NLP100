import sys
from package import func
# import linecache
# 今回は使わない

args = sys.argv
print(args)
print('対象ファイル:' + args[1])
print('カウント数:' + args[2])
intN = int(args[2])
list_box = []

with open(args[1]) as names:
    for re_line in names:
        list_box.insert(0, re_line)
    func.print_line(zip(list_box, range(intN)))


    # target_line = linecache.getline(names, int(intN))
    # print(target_line)
    # linecache.clearcache()
    # なぜか動かないし使わない。
