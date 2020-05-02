x = 0
y = 2
z = 1

if x % 2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditional')

if x % 2 == 0:
    if x % 3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x % 3 == 0:
    print('Divisible by 3 and not by 2')

if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')
