name = input("ФИО: ")
initials = ""
for i in name:
    if i.isupper():
        initials += i
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(name)}")