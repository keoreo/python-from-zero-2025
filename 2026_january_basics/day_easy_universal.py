age = 28
height = 1.78
name = 'Алексей'
is_student = True
city = "Кострома"
color = "Синий"

print("Возраст: ", age, type(age))
print("Рост: ", height, type(height))
print("Имя: ", name, type(name))
print("Учусь: ", is_student, type(is_student))
print("Город: ", city, type(city))
print("Любимый цвет :", color, type(color))

older = age + 5
print("Через 5 лет: ", older)

greeting = "Привет" + name + "!"
print(greeting)

working = not is_student
print("Работаю: ", working)