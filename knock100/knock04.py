str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. \
    New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
# str = str.replace('.', '')
to_split = str.split()
l1 = [1, 5, 6, 7, 8, 9, 15, 16, 19]
count = 0
# dd = {}
dict = {}
for word in to_split:
    count += 1
    if count not in l1:
        word = word[:2]
    else:
        word = word[0]
    dict[count]= word
#     dd[count] = word
#     dict.update(dd)
print(dict)
#
#
# print(to_split)
# print(dict)
