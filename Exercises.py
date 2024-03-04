#Exercise 1
new_list = ['Anna', 'Maria', 'Elizabeth', 'Chloe']
new_tuple = ('Python Assignment', 'exercises', 'tuple example')
new_float = 13.66
new_integer = 20
from decimal import Decimal
new_decimal = Decimal(35.47)
new_dictionary = {
    'first': 'John',
    'second': 'Max',
    'third': 'David',
    'fourth': 'George',
}

print(new_list)
print(new_tuple)
print(new_float)
print(new_integer)
print(new_decimal)
print(new_dictionary)

#Exercise 2
import math

print(round(new_float))

#Exercise 3
print(math.sqrt(new_float))


#Exercise 4
#Selected the first key-value pair
dictionary_groupings = new_dictionary.items()
print(list(dictionary_groupings)[0])   

#Selected the first key
print(list(new_dictionary.keys())[0])  

print(list(dictionary_groupings)[0][0])

#Selected the first value
first_value = new_dictionary['first']
print(first_value)                     

print(list(new_dictionary.values())[0])  

print(list(dictionary_groupings)[0][1])


#Exercise 5
print(new_tuple[1])

first, second, third = new_tuple
print(second)

#Exercise 6
new_list.extend(['Diana'])
print(new_list)

'''
another option

new_list.append('Diana')
print(new_list)
'''

#Exercise 7
new_list[0] = 'Dasha'
print(new_list)

#Exercise 8
new_list.sort()
print(new_list)

#Exercise 9
new_tuple += ('reassignment',)
print(new_tuple)

