"""
Простой тест: Hello World с версией Python.
Автор: keoreo
Дата: 2025-12-15
"""

def greet(name: str) -> str:
    """Возвращает приветствие."""
    return f"Hello, {name}!"

def main() -> None:
    """Точка входа."""
    print(greet("keoreo"))  # Фиксированное имя для теста
    print("Версия Python:", __import__("sys").version)

if __name__ == "__main__":
    main()