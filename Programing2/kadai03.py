def bisection(x, epsilon=0.01):
    epsilon1 = 0.01
    numGuesses1 = 0
    low1 = 0.0
    high1 = max(1.0, x)
    ans1 = (high1 + low1) / 2.0
    while abs(ans1 ** 2 - x) >= epsilon:
        print('low = ', low1, 'high =', high1, 'ans =', ans1)
        numGuesses1 += 1
        if ans1 ** 2 < x:
            low1 = ans1
        else:
            high1 = ans1
        ans1 = (high + low) / 2.0


if __name__ == '__main__':
    x = 25
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans**2 - x) >= epsilon:
        print('low = ', low, 'high =', high, 'ans =', ans)
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print('numGuesses =', numGuesses)
    print(ans, 'is close to square root of ', x)
