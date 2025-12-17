# первая часть задания

my_int = 3
my_float = 3.5
my_str = "привет"
my_bool = True
my_tuple = (10, 20.3)

"""
my_str[0] = 'X'
вызовет ошибку изменения не изменяевого объекта
"""

print(my_int)

my_int += 1

print(my_int)


# вторая часть задания

my_list = [1, 2, 3, 4, 5] # список
my_list.append(6) # добавляем новое значение
print(id(my_list))

my_dict = {1: 'one', 2: 'two'}
my_dict[2] = 'no two'
print(id(my_dict))

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(id(my_set))
