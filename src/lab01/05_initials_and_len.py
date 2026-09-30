name = input("ФИО: ")
initials = ""
for i in name.split():
    initials += i[0].upper()
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(name)}")
