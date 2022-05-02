import csv
from add_sale import add_salo
from show_sales import show_all, show_to, show_from_to
from change_sale import pomenyai_me_all


list_out = list()
first_list = list()
second_list = list()
change = int()
while change != 10:
    change = int(input("1) Ввести значение \n2) Вывести все значения \n3) Вывести все значения ДО какого-то номера \n4) Вывести значения из промежутка С\ДО \n5) Удалить все записи \n6) Захотелось поменять значение элемента? \n10) Выход\n"))
    change_add = 2
    if change == 1:
        while change_add != 1:
            if change_add == 2:
                list_out.clear()
                list_out = add_salo(first_list)
                print("Значение добавлено!\n")
                with open('bakery.csv', 'a', encoding='utf-8', newline='') as fw:
                    writer = csv.writer(fw)
                    writer.writerow(list_out)
            change_add = int(input("1) Мне хватит \n2) Еще по одной\n"))
    elif change == 2:
        show_all()
    elif change == 3:
        show_to()
    elif change == 4:
        show_from_to()
    elif change == 5:
        with open('bakery.csv', 'w'):
            print("Спец.отряд успешно провел операцию по зачистке файла\n")
    elif change == 6:
        pomenyai_me_all()


