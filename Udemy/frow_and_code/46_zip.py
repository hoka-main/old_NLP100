days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# for i in range(ren(days)):
#     print(days[i],fruit[i], drink[i])
for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)