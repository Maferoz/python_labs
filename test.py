fio= "Aaaa aAAAA aaaa aaaaa"
new_fio = []
fio = fio.strip()
for i in fio.split():
    new_fio.append(i.capitalize())
name = new_fio[0] 
    # Найдем инициаллы
print(new_fio)

