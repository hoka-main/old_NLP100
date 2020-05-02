def test_fanc(x, l=None): # listやdictはバグにつながりやすい
    if l is None:
        l = []
    l.append(x)
    return l

'''
y = [1, 2, 3]
r = test_fanc(100, y)
print(r)

y = [1, 2, 3]
r = test_fanc(200, y)
print(r)
'''

r = test_fanc(100)
print(r)

r = test_fanc(100)
print(r)