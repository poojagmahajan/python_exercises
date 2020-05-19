
##  Implement a calculateAvg function that receives the ages dictionary as a ​parameter,
# and returns the average age of the students.

def calculateAvg(ages):
  length=len(ages)      # len(dictionary) to calculate the length of dictionary,
  average = sum(ages.values())/length   # sum/length
   #print (length)
  return average  # sum(dictionary.values()) function to calculate the sum of values in a dictionary.
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
print(calculateAvg(ages))