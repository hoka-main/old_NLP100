str = 'Now I need a drink, alcoholic of course, after the heavy lextures involving quantum mechanics.'

str = str.replace(',','')
str = str.replace('.', '')

# print(str)
to_sprit = str.split(' ')
# print(to_sprit)
# help(list)
box = []
for a in to_sprit:
    box.append(len(a))
print(box)