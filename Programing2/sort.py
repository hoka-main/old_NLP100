from random import randint

global x
x = 0


def merge(left, right, compare):
    result = []

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[j])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    print(result)
    return result


def merge_Sort(L, compare=lambda x, y: x < y):
    global x
    x += 1
    print(x)
    if len(L) < 2:
        print(L)
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_Sort(L[:middle], compare)
        print(x, 'left: ', left)
        right = merge_Sort(L[middle:], compare)
        print(x, 'right: ', right)
        return merge(left, right, compare)


if __name__ == '__main__':
    L = [randint(1, 1000) for _ in range(10)]
    print(L)
    print(merge_Sort(L))
