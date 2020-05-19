


def find_students(address, students):
  names = []     ###Empty list
  for key, subdict in students.items():    # outer dict
       for sublist in subdict.values():    # inner
          if (sublist == address):
             names.append(key)    ## fill list
  return sorted(names)     # return sorted list

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
}
print(find_students("Lisbon", students))