tuple_ =tuple([1,2,3])
print(type(tuple_))
tuple_1 = ([1,2], 0)
tuple_1[0][1] = 4
print(tuple_1)
tuple_3 = (tuple_)*2 + tuple_1
print(tuple_3)
