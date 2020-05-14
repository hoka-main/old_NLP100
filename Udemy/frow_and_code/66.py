class UppercaseError(Exception):
    pass


def check():
    words = ['apple', 'banana', 'orange']
    for word in words:
        if word.isupper():
            raise UppercaseError

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')
