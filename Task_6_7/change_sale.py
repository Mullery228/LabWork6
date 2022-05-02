

def pomenyai_me_all():
    file_list = list()
    file_list.append("None")
    a = int(input("Номер какого элемента вы соизволите, мусье, изменить?\n"))
    while a < 1:
        print("Неправильно, введи номер больше 0")
        a = int(input("Номер какого элемента вы соизволите, мусье, изменить?\n"))
    with open('bakery.csv', 'r', encoding='utf-8') as fw:
        for line in fw:
            file_list.append(float(line))
    file_list[a] = float(input("Введите значение тут -> "))
    file_list.pop(0)
    new_list = [str(i) + '\n' for i in file_list]
    with open('bakery.csv', 'w', encoding='utf-8') as fw:
        fw.writelines(new_list)
        # writer = csv.writer(fw)
        # writer.writerow(new_list)
    print("Поздравляю! Такое можно и отметить")
