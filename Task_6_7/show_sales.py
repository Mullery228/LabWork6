

def show_all():
    with open('bakery.csv', 'r', encoding='utf-8') as fw:
        for line in fw:
            print(line)


def show_to():
    file_list = list()
    with open('bakery.csv', 'r', encoding='utf-8') as fw:
        for line in fw:
            file_list.append(line)
        a = int(input("До какого номера вы хотите вывести? - "))
        while a > len(file_list):
            print("Ты ввел номер, которого нет в списке, давай меньше вводи")
            a = int(input("До какого номера вы хотите вывести? - "))
        for i in range(a):
            print(file_list[i])

def show_from_to():
    file_list = list()
    file_list.append('None')  # чтобы нумерация начиналась с 1 (0 как бы есть, но его как бы None)
    a = 0
    b = 0
    with open('bakery.csv', 'r', encoding='utf-8') as fw:
        for line in fw:
            file_list.append(line)
        a = int(input("C какого номера начать?? - "))
        if a < 1:
            while a < 1:
                print("Давай по-новой и больше вводи больше 0 плиз")
                a = int(input("C какого номера начать?? - "))
        elif a > len(file_list) - 1:
            while a > len(file_list) - 1:
                print("Давай по-новой и вводи меньше", len(file_list), "плиз")
                a = int(input("C какого номера начать?? - "))
        b = int(input("До какого номера выводить? - "))
        if b < 1:
            while b < 1:
                print("Давай по-новой и вводи больше 0 плиз")
                b = int(input("До какого номера выводить? - "))
        elif b > len(file_list) - 1:
            while b > len(file_list) - 1:
                print("Давай по-новой и вводи меньше", len(file_list), "плиз")
                b = int(input("До какого номера выводить?? - "))
        if a > b:
            while a > b:
                print("Ты че, емае, начало должно быть не больше конца, го заново че)")
                a = int(input("C какого номера начать?? - "))
        for i in range(a, b + 1):
            print(file_list[i])

# НАДО ДОДЕЛАТЬ УСЛОВИЯ ДЛЯ 4 ВАРИАНТА ВВОДА