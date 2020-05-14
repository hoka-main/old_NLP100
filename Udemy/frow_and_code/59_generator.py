l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print('#############')

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

# for g in greeting():
#     print(g)
def counter(num=10):
    for _ in range(num):
        yield 'run'

c = counter()
g = greeting()
print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print(next(g))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(g))

