my_dict = ({'Mark': 2021, 'Keny': 2005, 'Selena': 2011})
print('Словарь', my_dict) #1 вывести список
my_dict = ({'Mark': 2021, 'Keny': 2005, 'Selena': 2011})
print(my_dict['Keny']) # 2 вывести из списка значение
print(my_dict.get('Kamila')) # 3 Такого ключа нет
my_dict.pop('Selena') # 3 удалить из списка
print(my_dict)
my_dict.update({'Max': 2003, 'Lena': 2006})
print(my_dict) # 4 добавить в список
print()
my_set = ({1, 4, 5, 4, 1, 5, False, 21,'яблоко', False, 21})
print(my_set)
my_set.add('string')
my_set.add('lost')
print(my_set)
print(my_set.remove('яблоко'))
print(my_set)
