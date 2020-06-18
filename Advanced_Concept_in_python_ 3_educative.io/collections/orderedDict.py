

# same as a dictionary but they remember the order in which items were inserted

'''Python’s collections module has another great subclass of dict known as OrderedDict. As the name implies, this dictionary keeps track of the order of the keys as they are added. If you create a regular dict,
you will note that it is an unordered data collection:'''

from collections import OrderedDict

ordered_dict  = OrderedDict() # or  ordered_dict = {}
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1

print(ordered_dict)
