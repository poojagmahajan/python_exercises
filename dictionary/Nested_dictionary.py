

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}
print (students)
print(students['Peter'])
print(students['Peter'] ['address'])
print(students['Peter'] ['age'])

for p_id,p_info in students.items() :
    print("\n name :" , p_id)
    for key in p_info:
        print(key + ':', p_info[key])
