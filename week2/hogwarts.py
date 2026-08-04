students = [
    {"name" : "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
    {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russel Terrier"},
    {"name" : "Draco", "house" : "Slytherin", "patronus" : None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")








# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor", 
#     "Draco": "Slytherin",
#     }

# for student in students:
#     print(student, students[student], sep=",")

#_____________________________

# for i in range(len(students)):
#     print(i + 1, students[i])

#_____________________________________

# for student in students:
#     print(student)

#________________________________

# print(students[0]) # Output: Hermione
# print(students[1]) # Output: Harry
# print(students[2]) # Output: Ron