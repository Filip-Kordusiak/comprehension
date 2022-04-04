numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Angela"
new_letter = [letter for letter in name]
print(new_letter)



lew_range = [n*2 for n in range(1, 5)]
print(lew_range)

names = ["Alex", "Filip", "Kuba"]
lew_list_if = [x.upper() for x in names if len(x) > 4]
print(lew_list_if)
import random
names = ["Alex", "Filip", "Kuba"]
students_scores = {x: random.randint(1, 100) for x in names}
print(students_scores)

pass_student = {x:score for (x, score) in students_scores.items() if score > 50}
print(pass_student)

student_dict = {
    "student": ["Alex", "Filip", "Kuba"],
    "score": [56,78,88]
}
for (key, values) in student_dict.items():
    print(values)



