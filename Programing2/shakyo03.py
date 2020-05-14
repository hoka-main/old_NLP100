# 求めたい平方根を代入する
x = 25
# epsilonに0.01を代入する
# (誤差を0.01以内に指定)
epsilon = 0.01
# step に epsilon を二乗して代入する
step = epsilon ** 2
# numGuesses にint型を指定する
numGuesses = 0
# ans にdouble型の変数を指定する
ans = 0.0

# ans**2 - x(近似値と仮定したもの)がepsilonよりも大きく　かつ　xよりも小さくなるまで
while abs(ans**2 - x) >= epsilon and ans <= x:
# ansにepsilonの二乗を+する
    ans += step
# numGuessesに+1する
    numGuesses += 1
# numGuesses(while分を繰り返した回数)を画面表示する
print('numGuesses =', numGuesses)
# ans**2 - x(近似値と仮定したもの) が epsilon よりも大きい場合
if abs(ans ** 2 - x) >= epsilon:
# x は平方根をオーバーしているよと伝える
    print('Failed on square root of', x)
# それ以外の場合
else:
# x は平方根よりも小さいよと伝える
    print(ans, 'is close to square root of', x)
