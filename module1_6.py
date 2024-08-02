# работа со словарём

my_dict = {'Никита': 2001, 'Максим': 1988, 'Данил': 2007}
print(my_dict)
print(my_dict['Никита'])
print(my_dict.get('Иван'))
my_dict.update({'Ирина': 2010,
                'Мария': 1999})
year = my_dict.pop('Максим')
print(year)
print(my_dict)

# работа с множествами

my_set = {2, 3, 4, 2, 'сом', 'рыба', 'сом'}
print(my_set)
my_set.add(6)
my_set.add('карп')
my_set.discard('сом')
print(my_set)
