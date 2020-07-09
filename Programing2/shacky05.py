def fib(x):
    global numFibCalls
    numFibCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def test_Fib(n):
    for i in range(n + 1):
        global numFibCalls
        numFibCalls = 0
        print('fib of', i, '=', fib(i))
        print('fib called ', numFibCalls, 'times.')


test_Fib(6)
