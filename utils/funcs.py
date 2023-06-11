import os
import json


def load_operations():
    """
    Возвращает список операций в формате json
    """
    with open(os.path.join("..", "operations", "operations.json"), encoding="utf-8") as f:
        f_content = f.read()
        return f_content


def last_five_exec_ops():
    """
    Возвращает список из 5 последних совершенных (EXECUTED) операций
    """
    operations = json.loads(load_operations())
    counter = 0
    exec_operations = []
    for operation in operations:
        if operation["state"] == "EXECUTED":
            counter += 1
            exec_operations.append(operation)
        if counter == 5:
            return exec_operations
    return exec_operations


def operations_sorted(operations):
    """
    Принимает на вход список из 5 последних совершенных (EXECUTED)
    операций и возвращает отсортированный по дате массив
    """
    operations_sorted = []
    while operations:
        max_operation = operations[0]
        max_y = int(max_operation["date"][0:4])
        max_m = int(max_operation["date"][5:7])
        max_d = int(max_operation["date"][8:10])
        max_index = 0
        for i in range(1, len(operations)):
            cur_y = int(operations[i]["date"][0:4])
            cur_m = int(operations[i]["date"][5:7])
            cur_d = int(operations[i]["date"][8:10])
            if cur_y > max_y:
                max_y, max_m, max_d = cur_y, cur_m, cur_d
                max_index = i
            elif cur_y == max_y:
                if cur_m > max_m:
                    max_y, max_m, max_d = cur_y, cur_m, cur_d
                    max_index = i
                elif cur_m == max_m:
                    if cur_d > max_d:
                        max_y, max_m, max_d = cur_y, cur_m, cur_d
                        max_index = i
        operations_sorted.append(operations[max_index])
        operations.pop(max_index)
    return operations_sorted


def correct_date(operation):
    """
    Принимает на вход отчет об одной операции в виде словаря
    и возвращает дату в верном формате
    """
    date = operation["date"]
    year = date[0:4]
    month = date[5:7]
    day = date[8:10]
    date_arr = [day, month, year]
    correct_date = ".".join(date_arr)
    return correct_date


def correct_card_name(operation):
    """
    Принимает на вход отчет об одной операции в виде словаря
    и возвращает имя карты без цифр
    """
    card_name = operation["from"]
    index_counter = 0
    for symbol in card_name:
        if symbol.isnumeric():
            return card_name[:index_counter], index_counter
        index_counter += 1
    return card_name, index_counter


def correct_card_info(operation):
    """
    Принимает на вход отчет об одной операции в виде словаря
    и возвращает имя и номер карты. Номер разбит на блоки, цифры скрыты в
    соответствии с заданием
    """
    card_info = operation["from"]
    card_name, index_counter = correct_card_name(operation)
    card_number = card_info[index_counter:]
    card_number_arr = [
        card_number[:4],
        card_number[4:8],
        card_number[8:12],
        card_number[12:16],
    ]
    card_number_arr[1] = card_number_arr[1][:2] + "**"
    card_number_arr[2] = "****"
    correct_card_number = " ".join(card_number_arr)
    correct_card_info = card_name + correct_card_number
    return correct_card_info


def correct_bank_account(operation):
    """
    Принимает на вход отчет об одной операции в виде строки
    и возвращает замаскированный счет получателя
    """
    correct_bank_account = "Счет **" + operation[-4:]
    return correct_bank_account


def print_message():
    """
    Выводит сообщения о пяти последних исполненных
    операциях в нужном формате
    """
    exec_operations = last_five_exec_ops()
    sorted_operations_arr = operations_sorted(exec_operations)
    for operation in sorted_operations_arr:
        if operation["description"] == "Открытие вклада":
            print(correct_date(operation), operation["description"])
            print(correct_bank_account(operation["to"]))
            print(operation["operationAmount"]["amount"], operation["operationAmount"]["currency"]["name"], "\n")
        else:
            if operation["from"][:5] == "Счет ":
                print(correct_date(operation), operation["description"])
                print(correct_bank_account(operation["from"]), "->", correct_bank_account(operation["to"]))
                print(operation["operationAmount"]["amount"], operation["operationAmount"]["currency"]["name"], "\n")

            else:
                print(correct_date(operation), operation["description"])
                print(correct_card_info(operation), "->", correct_bank_account(operation["to"]))
                print(operation["operationAmount"]["amount"], operation["operationAmount"]["currency"]["name"], "\n")
