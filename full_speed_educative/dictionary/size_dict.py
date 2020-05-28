
## Given a lengthDictionary function that takes Students dictionary as a parameter,
# find how many students are in the dictionary.

def lengthDictionary(Students):
  return len(Students)
Students = {
     "Peter": 10,
     "Isabel": 11,
     "Anna": 9,
     "Thomas": 10,
     "Bob": 10,
     "Joseph": 11,
     "Maria": 12,
     "Gabriel": 10,
}

print("\nsize :" , lengthDictionary(Students))