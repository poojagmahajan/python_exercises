
'''  counters on the list '''

from collections import Counter

counter_one = Counter('superfluous')
print (counter_one)
#Counter({'u': 3, 's': 2, 'l': 1, 'r': 1, 'e': 1, 'o': 1, 'p': 1, 'f': 1})

print (counter_one['u'])
#3

counter_two = Counter('super')
print(counter_one.subtract(counter_two))
#None

print (counter_one)
#Counter({'u': 2, 'l': 1, 'o': 1, 's': 1, 'f': 1, 'r': 0, 'e': 0, 'p': 0})

print (list(counter_one.elements()))
#['u', 'u', 'u', 'o', 'p', 'e', 'f', 'l', 'r', 's', 's']

print( counter_one.most_common(2))
#[('u', 3), ('s', 2)]

a  = 'aaabbbbcccccc'
my_counter = Counter(a)
print(my_counter)  # it will return dictionary
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(3))
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))






