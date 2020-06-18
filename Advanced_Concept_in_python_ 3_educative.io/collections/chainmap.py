
#'''Python’s collections module has specialized container datatypes
# that can be used to replace Python’s general purpose containers (dict, tuple, list, and set)'''

'''
A ChainMap is a class that provides the ability to link multiple mappings together
such that they end up being a single unit. If you look at the documentation,
 you will notice that it accepts **maps*, which means that a ChainMap will accept any number of mappings
 or dictionaries and turn them into a single view that you can update.

'''

from collections import ChainMap

car_parts = {'hood': 500, 'engine': 5000, 'front_door': 750}
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = {'cover': 100, 'hood_ornament': 150, 'seat_cover': 99}
car_pricing = ChainMap(car_accessories, car_options, car_parts)
print (car_pricing['hood'])
#500
print(car_pricing)