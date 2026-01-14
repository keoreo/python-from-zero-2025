"""
day01_rep_01_basic_operations.py
Демонстрация арифметических и логических операций
"""

name: str = "Кирилл"
age: int = 24
city: str = "Кострома"
is_happy: bool = True
university: str = "МУБИНТ"
hour: int = 12
minute: int = 32
height: float = 1.89

print(f"Имя: {name}")
print(f"Возраст: {age}")
print(f"Город: {city}")
print(f"Университет: {university}")
print(f"Время: {hour}:{minute}")
print(f"Рост: {height}")

age_later = age + 10
print(f"Через 10 лет мне будет {age_later}")

minute_later = minute + 20
print(f"Через 20 минут будет {hour}:{minute_later}")

height_cm = height * 100
print(f"Рост в сантиметрах: {height_cm}")
