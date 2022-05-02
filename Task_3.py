import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    # Ваш код пишите здесь
    first_list = list()
    second_list = list()
    with open('users.csv', 'r', encoding='utf-8') as path_users_file:
        # data_one = read_user.read()
        # print(sys.getsizeof(data_one))
        with open('hobby.csv', 'r', encoding='utf-8') as path_hobby_file:
            # data_two = read_hobby.read()
            # print(sys.getsizeof(data_two))
            for first_line in path_users_file:  # при переборе строк файла, для оптимизации ОЗУ, напрямую перебираем строки из файла, не используя посредника, чтобы вся инфа сразу не записывалась в ОЗУ, т.к посредник сразу записывает в себя все строки
                first_list.append(first_line.replace(',', ' '))  # убираем запятые в ФИО, т.к используем всего 1 ячейку сразу под всё ФИО. Формируем список строк, полученных из файла
            for second_line in path_hobby_file:
                second_list.append(second_line) # тут просто формируем список хобби
            if len(first_list) == len(second_list): # проверяем длину списков
                dickt = dict(zip(first_list, second_list)) # если всё гуд, то зипуем два списка в словарь
            elif len(first_list) > len(second_list): # если юзерсов больше, чем хобби(или они просто любят ничего не делать)
                for i in range(len(first_list) - len(second_list)): # в список хобби просто добавляем Ноне до того момента, пока списки не будут равны
                    second_list.append('None')
                dickt = dict(zip(first_list, second_list))  # зипуем два списка в словарь
            else:
                return 1  # на случай, если всё плохо
    # print(sys.getsizeof(dickt))
    return dickt  # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
