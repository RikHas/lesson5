print('Работа со списками:')
my_list = ['apple', 'pear', 'melon', 'mango', 'watermelon']
print('List: ', my_list)
print('First element: ',my_list[0])
print('Last element: ',my_list[-1])
print('Sublist: ',my_list[2:5])
my_list[2] = 'avocado'
print('Modified list: ',my_list)
print()
print('Работа со словарями:')
my_dict = {'apple':'яблоко', 'pear':'груша', 'melon':'дыня', 'mango':'манго', 'watermelon':'арбуз'}
print('Dictionary: ', my_dict)
print('Translation: ', my_dict.get('mango'))
my_dict.update({'kiwi':'киви'})
print('Modified dictionary: ', my_dict)