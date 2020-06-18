
'''
The collections module has a handy tool called defaultdict.
The defaultdict is a subclass of Python’s dict that accepts a default_factory as its primary argument.
The default_factory is usually a Python type, such as int or list,
 but you can also use a function or a lambda too.
  Let’s start by creating a regular Python dictionary that counts the number of times each word is used in a sentence:
'''

sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

reg_dict = {}
for word in words:
    if word in reg_dict:
        reg_dict[word] += 1
    else:
        reg_dict[word] = 1

print(reg_dict)

# using defaultdict

from collections import defaultdict


sentence = "The red for jumped over the fence and ran to the zoo for food"
words = sentence.split(' ')

d = defaultdict(int)
for word in words:
    d[word] += 1

print(d)

## 1 - List Type

my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

reg_dict = {}
for acct_num, value in my_list:
    if acct_num in reg_dict:
        reg_dict[acct_num].append(value)
    else:
        reg_dict[acct_num] = [value]

print(reg_dict)

# using defaultdict

from collections import defaultdict


my_list = [(1234, 100.23), (345, 10.45), (1234, 75.00),
           (345, 222.66), (678, 300.25), (1234, 35.67)]

d = defaultdict(list)
for acct_num, value in my_list:
    d[acct_num].append(value)

print(d)

# using Lambda

from collections import defaultdict
animal = defaultdict(lambda: "Monkey")
animal['Sam'] = 'Tiger'
print (animal['Nick'])
#Monkey

print (animal)
#defaultdict(<function <lambda> at 0x7f32f26da8c0>, {'Nick': 'Monkey', 'Sam': 'Tiger'})

## returns default value of type if dict is empty

from collections import defaultdict

d = defaultdict(int)  # int is default type here
d['a'] = 1
d['b'] =  2

print(d['a'])
print(d['c'])   # returns default value of int i.e. 0 , incase of normal dict it will throw error