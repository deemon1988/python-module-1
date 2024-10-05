from os import remove
from random import shuffle

from unicodedata import digit

food = ["apple", "coconut", "banana"]
food.append(True)
food.extend(['string', 12])

print(food)
print("coconut" not in food)
food.remove("apple")
print("apple" in food)

food.clear()
food.append("tomato")
food.extend(["apple", "coconut"])
print("Список до добавления",food)
food.extend([1])
print("Список после",food)
print("Индекс числа 1 -",food.index(1))
food.insert(0,'-')
food.insert(len(food),2)
food.remove('-')
removed_item = food.pop(0)
print("Метод pop() вернул - ",removed_item)
food.insert(5,3)
print("Индекс числа 1 -", food.index(1))
print(food.index(2))

print(food)
food.append(3)
print(food.count(3))

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

sorted_list.reverse()
print(sorted_list)


copy_list=list.copy(sorted_list)
copy_list.reverse()
print(copy_list)


