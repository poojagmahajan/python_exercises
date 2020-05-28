

## Implement an updateAges function that receives ages dictionary and
# a number n and returns a new dictionary where each student is (n) years older.

def updateAges(ages, n):
  new_ages = {}
  for word in ages:
    new_ages[word] = ages[word] + n
  return new_ages
ages = {
      "Peter": 10,
      "Isabel": 11,
      "Anna": 9,
      "Thomas": 10,
      "Bob": 10,
      "Joseph": 11,
      "Maria": 12,
      "Gabriel": 10,
   }
new_ages = updateAges(ages, 10)

print(new_ages)