# === Этап 1. Самый простой уровень ===

# Целые числа
vlan_id = 10
mask = 24

# Вещественные числа
temperature = 36.6

# Строки
hostname = "switch01"
interface = "GigabitEthernet0/0/1"

# Логические типы
is_up = True
is_trunk = False

# Вывод данных
print("vlan_id: ", vlan_id, type(vlan_id))
print("temperature: ", temperature, type(temperature))
print("hostname: ", hostname, type(hostname))
print("is_up: ", is_up, type(is_up))

# Простейшие операции
total_vlans = vlan_id + 5
print("total_vlans: ", total_vlans)

full_name = hostname + ".borjomi.local"
print("full_name: ", full_name)

status = is_up and not is_trunk
print("Доступный порт: ", status)

