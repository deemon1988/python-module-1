sorted_list = sorted([1,5,3,8,2,9,1,4,8,2,7,4,8,3,2,1,8,9])
print(sorted_list)
shuffle(sorted_list)
print(sorted_list)
sorted_list.sort()
print(sorted_list)
print(sorted({2: 'D', 3: 'B', 1: 'B', 5: 'E', 4: 'A'}))
sorted_list = sorted("This is a test string from Andrew".split(), key=str.casefold)
print(sorted_list)

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print(sorted(student_tuples, key=lambda student: student[2]))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.


                     Student('john', 'A', 15),
                     Student('jane', 'B', 12),
                     Student('dave', 'B', 10),
                     sorted(student_objects, key= lambda student: student.age)))