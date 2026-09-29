def format_record(rec: tuple[str,str,float]) -> str:
    fio, group, gpa = rec
    '''
    if type(fio) != str:
        raise ValueError("ФИО должно быть строкой")
    if type(group) != str:
        raise ValueError("Группа должна быть строкой")
    if type(gpa) != int and type(gpa) != float:
        raise ValueError("GPA должен быть числом")
    if gpa < 0 or gpa > 5:
        raise ValueError('Неверный GPA')
    '''
    fio = fio.strip() #минус лишние пробелы
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
    