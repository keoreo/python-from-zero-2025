# Задача 1
vlan_input = str(input("Введите строку типа 'Vlan 100': "))
print(f"VLAN: {vlan_input}")

# Задача 2
mask_str = "255.255.255.0"

# Задача 3 — генерация конфига
vlan = 200
descr = "Uplink-to-Core"
print("interface GigabitEthernet0/0/5")
print(f" port default vlan {vlan}")
print(f" description {descr}")