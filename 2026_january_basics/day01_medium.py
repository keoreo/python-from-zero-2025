"""
Этап 2. Средний уровень сложности
Переменные, типы, преобразования, сравнения
"""

# Аннотация типов данных
hostname: str = "SW-Huawei-01"
vlan: int = 100
mask: int = 24
itilization: float = 67.8
is_active: bool = True
port_sfp: str = "10Gb"
id_port: int = 43

# Преобразование
vlan_str = str(vlan)
mask_float = float(mask)
active_str = "active" if is_active else "down"
itilization_int = int(itilization)
id_port_float = float(id_port)

# Вывод в красивом виде
print(f"Устройство: {hostname.upper()}")
print(f"VLAN: {vlan} (строкой: {vlan_str})")
print(f"Маска: /{mask}, в float: {mask_float}")
print(f"Загрузка интерфейса: {itilization:.1f}%")
print(f"Активный порт: {id_port}")
print(f"Порт SFP: {port_sfp}")

# Сравнение
a = 100
b = 100
c = 100.0

print("a == b ->", a == b)
print("a is b ->", a is b)
