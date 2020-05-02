def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)
    # for k, v in kwargs.items():
    # print(k, v)

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')

'''
d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)
'''