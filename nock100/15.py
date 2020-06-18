import sys
import linecache

args = sys.argv

print(args)
# if args is int:
print('第1引数:' + args[1])
intN = args[1]
with open('popular_names.txt') as names:
    target_line = linecache.getline(names, int(intN))
    print(target_line)
    linecache.clearcache()
# else:
print('第1引数:' + args[1])
print('int型の自然数 N を引数として入力してください。')
