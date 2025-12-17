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
print(id(my_list))

my_list.append(6) # добавляем новое значение
print(id(my_list))

my_dict = {1: 'one', 2: 'two'}
print(id(my_dict))

my_dict[2] = 'no two'
print(id(my_dict))

my_set = {1, 2, 3, 4, 5}
print(id(my_set))

my_set.add(6)
print(id(my_set))


# Третья часть задания

print("\n=== 3. Проблема мутабельных параметров по умолчанию ===")

def bad_func(config: list = []) -> list:
    """Плохая функция: Список по умолчанию мутабелен."""
    config.append("new_item")
    return config

# Демонстрация бага
result1 = bad_func()
result2 = bad_func()
print("Результат 1:", result1)
print("Результат 2:", result2)
print("ID result1:", id(result1))
print("ID result2:", id(result2))
print("(Объяснение: список [] созданный один раз при определении функции)\n")

print("=== 4. Правильное решение ===")

def good_func(config: list | None = None) -> list:
    """Хорошая функция: используем None и создаём новый список внутри."""
    if config is None:
        config = []
    config.append("new_item")
    return config

# Демонстрация исправления
result3 = good_func()
result4 = good_func()
print("Результат 3:", result3)
print("Результат 4:", result4)
print("ID result3:", id(result3))
print("ID result4:", id(result4))  # ID разные — списки независимые
print("(Объяснение: новый список создаётся при каждом вызове)")