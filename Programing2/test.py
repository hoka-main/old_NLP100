pi = 3.14
print(pi,type(pi))
pi = '円周率'
print(pi, type(pi))

side = 1  # 正方形の1辺の長さ
radius = 1  # 円の半径
pi = 3.14
# 正方形の面積から円の面積を引く
areaC = pi * radius ** 2
areaS = side * side
difference = areaS - areaC
print(difference)

x = 100
y = 300
print('x=', x)
print('y=', y)
x, y = y, x
print('x=', x)
print('y=', y)

box = x
x = y
y = box
print('x=', x)
print('y=', y)
