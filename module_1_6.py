my_dict = {'Pasha': 1988, 'Nina': 1991, 'Max': 1990}
print(my_dict)
print(my_dict['Pasha'])
my_dict['Anton'] = 1967
print(my_dict)
my_dict.update({'Bil': 1967, 'Jonn': 1956})
print(my_dict)
del my_dict['Anton']
print(my_dict)
my_set = {1,4,1,4,3,6,3,2,2,'Pasha','Jonn'}
print(my_set)
print(my_set.add(5))
print(my_set.add('Mike'))
print(my_set)
print(my_set.discard(1))
print(my_set)