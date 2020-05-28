# “paraparaparadise”と”paragraph”に含まれる
# 文字bi-gramの集合を，それぞれ, XとYとして
# 求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，’se’というbi-gramがXおよびYに含まれる
# かどうかを調べよ．
def n_gram(str, n):
    return [str[bit:bit + n] for bit in range(len(str) - n + 1)]

sample1 = 'paraparaparadise'
sample2 = 'paragraph'

X = n_gram(sample1, 2)
Y = n_gram(sample2, 2)

print(X + Y)

X_and_Y = set(X) & set(Y)
print(X_and_Y)

X_Y_diff = set(X) ^ set(Y)
print(X_Y_diff)
# se がXとYに含まれているかの問いに対して
print('X =', 'se' in X)
print('Y =', 'se' in Y)
