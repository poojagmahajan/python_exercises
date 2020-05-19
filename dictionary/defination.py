

### Dictionaries are data structures that index values by a given key (key-value pairs).


ages = {
    "purvansh" : 3,
    "Pooja"    : 28,
    "Gaurav"   : 30,
    "swarit"   : 1 ,
    "meet"     : 10,
    "ishan"    : 6
}

print("print age of any one -")
print (ages ["purvansh"])
print(ages["Gaurav"])

print("\n print ages of all -")
for name,age in ages.items() :
    print(name,age)

address = {}  #Call dictionary with no parameters using the empty {}

pincode = dict()    #Call dictionary with no parameters using the dict keyword

address["pooja"] = "pune"    ## fill to empty dictionary
address["purvansh"] = "chinchwad"

for name,address in address.items() :
    print("\n", name,address)

d = {     ## dictionary keys can be immutable object and don’t necessarily need to be strings
    0: [0, 0, 0],
    1: [1, 1, 1],
    2: [2, 2, 2],
}

print ( d[2] )


##You can create an ordered dictionary which preserves the order in which the keys are inserted.
# This is done by importing the OrderedDictionary from the collections library, and call the OrderedDictionary() built-in method.

from collections import OrderedDict

ages = OrderedDict()

ages["ram"] = 20
ages["sham"] = 40

for key, value in ages.items():
    print(key, value)

#####Loop to Get All Keys

for key in ages:  #for name in ages
  print(key)

####or

print(ages.keys())

##### Loop to Get All Values

for age in ages :      # for value in ages :
    print(ages[age])

#### or

print (ages.values())
######################################

Dict1 = {
  "FruitName": "Mango",
  "season": "Spring",
}
Dict1.pop("season")    ## pop delete value
print(Dict1.values())

print (Dict1)    ## print whole dictionary
print (Dict1.values())
print(Dict1.keys())

Dict1.clear()  # delete Dict

print(Dict1)  # will print empty paranthesis {}
