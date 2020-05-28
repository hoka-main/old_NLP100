import time



def factI(n):
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result

def factR(n):
    if n == 1:
        return n
    else:
        return n * factR(n - 1)


start_time = time.time()
print(factI(100))
end_time = time.time()
print(end_time - start_time)

start_time = time.time()
print(factR(100))
end_time = time.time()
print(end_time - start_time)
