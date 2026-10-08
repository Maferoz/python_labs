def format_record(rec: tuple[str,str,float]) -> str:
    fio, group, gpa = rec
    fio = fio.strip()
    if type(fio) != str or len(fio) == 0:
        raise ValueError("Неверное ФИО")
    if type(group) != str or len(group.strip()) == 0:
        raise ValueError("Неверная Группа")
    if (type(gpa) != int and type(gpa) != float) or gpa < 0 or gpa > 5:
        raise ValueError("Неверный GPA")
    new_fio = []
    for i in fio.split(): #делаем список с красивым фио
        new_fio.append(i.capitalize())
    name = new_fio[0] #берем из него фамилию
    initials = ""
    for i in new_fio[1:]: #берем из него инициалы без фамилии
        for j in i:
            if j.isupper():
                initials = initials + j + "."
    result = f"{name} {initials},гр. {group}, GPA {gpa:.2f}"
    return result
case1 = ("  1   ", "      1    ", 5)
print(format_record(case1))

    