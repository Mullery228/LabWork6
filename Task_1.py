

# Создаю и использую второй файл для вывода подходящих строк, т.к консоль пейчара не может вывести такое кол-во строк(она начинает удалять первые строки, чтобы добавить новые)

count = 0
with open('out.txt', 'w', encoding='utf-8') as outist:
    with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
        for line in fr:
            count += 1
            list_out = list()
            remote_addr = str()
            request_type = str()
            requested_resource = str()
            for i in range(len(line)):  # тут ищем IP адрес в строке
                if line[i] != ' ':
                    remote_addr += line[i]
                else:
                    break
            list_out.append(remote_addr)
            for i in range(len(line)):  # а тут уже ищем название запроса
                if line[i] == "G" and line[i + 1] == "E" and line[i + 2] == "T":
                    request_type = "GET"
                elif line[i] == "H" and line[i + 1] == "E":
                    request_type = "HEAD"
            list_out.append(request_type)
            for i in range(len(line)):  # а тут смотрим путь файла
                if line[i] == "d" and line[i + 1] == "o" and line[i + 2] == "w":
                    while line[i] != ' ':
                        requested_resource += line[i]
                        i += 1
            list_out.append(requested_resource)
            outist.write(str(list_out) + '\n')
