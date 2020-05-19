

## Implement an oldestStudent function that receives the ages dictionary as a parameter,
# and returns the name of the oldest student

##  Create a list containing values and another list containing keys.
## Get the maximum index of values using the max() built-in function.
# Then, using key[value.index(max(value))


def oldestStudent(ages):
    value = list(ages.values())
    key = list(ages.keys())
    max_value = key[value.index(max(value))]

    return max_value

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
print(oldestStudent(ages))