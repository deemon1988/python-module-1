#  Практическое задание по теме: "Словари и множества"

my_dict = {'Dmitriy': 1988, 'Denis': 1993, 'Andrew': 1998}
print('Dict:',my_dict)
print('Existing value:',my_dict['Dmitriy'])
print('Not existing value:',my_dict.get('Max'))
my_dict.update({'Alex': 1990, 'Anton': 1991})
a = my_dict.pop('Anton')
print('Deleted value:',a)
print('Modified dictionary:',my_dict)

my_set = {2,3,4,3,2,1, 'string', 'string', False, False, True, (1,2,3), (1,2,3)}
print('Set:',my_set)
my_set.update(['hello', 1987])
my_set.remove(1)
print('Modified set:',my_set)



