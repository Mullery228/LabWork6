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
    finally_list = list()
    with open('users.csv', 'r', encoding='utf-8') as path_users_file:
        with open('hobby.csv', 'r', encoding='utf-8') as path_hobby_file:
            for line in path_users_file:  # При переборе строк файла, для оптимизации ОЗУ, напрямую перебираем строки из файла, не используя посредника, чтобы вся инфа сразу не записывалась в ОЗУ, т.к посредник сразу записывает в себя все строки
                first_list.append(line)  # Формируем список строк, полученных из файла
            first_tuple = tuple(first_list)  # Переводим в кортеж, чтобы оптимизироваться по памяти(кортеж хорошо подойдет(для оптимизации памяти) именно для хранения огромного кол-ва элементов)
            first_list.clear()  # Ликвидируем объект
            for line in path_hobby_file:
                second_list.append(line)  # Формируем список хобби
            if len(first_tuple) == len(second_list):  # проверяем длину списков
                second_tuple = tuple(second_list)  # Переводим в кортеж, чтобы оптимизироваться по памяти
                second_list.clear()  # Ликвидируем объект
                for i in range(len(first_tuple)):
                    finally_list.append(first_tuple[i] + ": " + second_tuple[i])
            elif len(first_tuple) > len(second_list):  # если юзерсов больше, чем хобби(или они просто любят ничего не делать)
                for i in range(len(first_tuple) - len(second_list)):  # в список хобби просто добавляем Ноне до того момента, пока кортеж и список не будут равны
                    second_list.append('None')
                finally_list = first_tuple[i] + ": " + second_list[i]
            else:
                return 1  # на случай, если всё плохо
    # print(finally_list)
    return finally_list  # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_4_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
