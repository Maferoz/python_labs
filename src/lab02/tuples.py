def format_record(rec: tuple[str,str,float]) -> str:
    fio, group, gpa = rec
    if type(fio) != str or len(fio.strip()) == 0: # ФИО должно быть непустой строкой
        raise TypeError("Неверное ФИО")
    if len(fio.split()) <= 1: # ФИО из 1-го слова тоже не подойдет
        raise ValueError("Неверное ФИО")
    if type(group) != str or len(group.strip()) == 0: #Группа должна быть непустой строкой
        raise TypeError("Неверная Группа")
    if (type(gpa) != int and type(gpa) != float) or gpa < 0 or gpa > 5: # 0 <= GPA <= 5
        raise TypeError("Неверный GPA")
    # Удаляем лишние пробелы
    fio = fio.strip()
    group = " ".join(group.split()) # strip убирает лишние пробелы только по краям
    # Сделаем fio приемлимым
    new_fio = [] # список с ФИО, 1 заглавная, остальные маленькие, пробелы норм
    for i in fio.split():
        new_fio.append(i.capitalize())
    name = new_fio[0] 
    # Найдем инициаллы
    initials = ""
    new_fio = new_fio[1:]
    for i in new_fio:
        initials += i[0] + "."
    if len(initials) > 4:
        initials = initials[:4]

    # Формулируем результат
    result = f"{name} {initials}, гр. {group}, GPA {gpa:.2f}"
    return result
case1 = (" 1111 1111 1111", "1     1", 5)
print(format_record(case1))

    