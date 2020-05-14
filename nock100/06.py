def n_gram(str, n):
    return [str[bit:bit + n] for bit in range(len(str) - n + 1)]

sample1 = 'paraparaparadise'
sample2 = 'paragraph'

word1 = sample1.split()