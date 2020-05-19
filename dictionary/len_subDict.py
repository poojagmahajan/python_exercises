

def totalStudents(students):
  return(len(students.keys()))
  ## OR    return len(students)

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
}
print(totalStudents(students))