# Строки и Индексация строк
from email.policy import strict

# name = "Dmitriy"
# print(name[-1])
# print(name[0:4:3])
# print(name[::-1])

# Методы строки

new_my_string = "hello world! {}"
print(new_my_string.capitalize())
print(new_my_string.center(20,'*'))
print(new_my_string.count('world',6))
print(new_my_string.count('',1))
print(new_my_string.encode(encoding="UTF-16"))
print(new_my_string.endswith('w',0,7))
print(new_my_string.find('ello'))
#print(new_my_string.index('elo'))
print(new_my_string.format("world"))
print("The sum of 1 + 2 is {0}".format(1+2))

s = "My name is {name} and I am {age} years old, I'm learning {lang}"
my_dict = {'name': 'Dmitriy', 'age': '35', 'lang': 'python'}
print(s.format_map(my_dict))
print(s.format(**my_dict))

word = 'institution kitchen'
print (word.isalnum())  # Вернёт False, так как пробел не является буквенно-цифровым символом
word = 'institution4kitchen'
print (word.isalnum())  # Вернёт True
word = 'institutionkitchen'
print(word.isalpha())
word = 'Привет'
print(word.isascii())
word = '123'
print(word.isdecimal())
word = '\u00B3345'
print(word)
print(word.isdigit())
word = 'X\u2071'
print(word)

s = "hello World"
print(s.islower())
s = "HELLO WORLD"
print(s.isupper())
print(s.isprintable())
s = ' '
print(s.isspace())
s = 'Python Is Good.'
print(s.istitle())
s = 'Python is good'
print(s.istitle())










