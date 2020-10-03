def n_gram(str,n):
    return [str[bit:bit + n] for bit in range(len(str) - n + 1)]

sample = 'I am an NLPer'

print(n_gram(sample,1))
print(n_gram(sample,2))
print(n_gram(sample,3))
print(n_gram(sample,4))
print(n_gram(sample,5))


word = sample.split(' ')

print(n_gram(word, 1))
print(n_gram(word, 2))
print(n_gram(word, 3))