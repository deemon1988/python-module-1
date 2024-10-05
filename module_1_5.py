# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

immutable_var = (1, 'string', True, [1, 2, 3])
print("Immutable tuple:", immutable_var)
# immutable_var[0] = 2 # объекты типа 'tuple' (кортеж) не поддерживают изменения,
# нельзя назначить элементу с индексом [0] новое значение

mutable_list = ['banana', 'tomato', 2]
mutable_list[0] = 'apple'
mutable_list.append('coconut')
mutable_list.extend([1, True, 'hello'])
print("Mutable list:", mutable_list)
