list_length = int(input("Введите длину списка: "))
list_1 = []

for i in range(list_length):
    index = i + 1
    index_suffix = "ое"
    
    if (index % 10 == 2) and (index % 100 != 12):
        index_suffix = "ье"
    
    number = int(input(f"Введите {index}-{index_suffix} число: "))
    list_1.append(number)

print(list_1)

list_1 = []
for i in range(int(input("Введите длину списка: "))):
    if i == 2 + 10 * (i // 10) and i != 12 + 100 * (i // 100):
        list_1.append(int(input(f"Введите {i + 1}-ье число: ")))
    else:
        list_1.append(int(input(f"Введите {i + 1}-ое число: ")))
print(list_1)
