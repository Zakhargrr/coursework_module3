import utils.funcs as funcs
import pytest


@pytest.fixture
def five_elem_dict():
    return [{
        "id": 649467725,
        "state": "EXECUTED",
        "date": "2018-04-14T19:35:28.978265",
        "operationAmount": {
            "amount": "96995.73",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 27248529432547658655",
        "to": "Счет 97584898735659638967"
    },
        {
            "id": 34148726,
            "state": "EXECUTED",
            "date": "2018-11-23T23:52:36.999661",
            "operationAmount": {
                "amount": "79428.73",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 5355133159258236",
            "to": "Maestro 8045769817179061"
        },
        {
            "id": 636137913,
            "state": "EXECUTED",
            "date": "2019-06-16T22:17:01.825020",
            "operationAmount": {
                "amount": "24260.78",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Platinum 8990850370884895",
            "to": "Счет 15574304810835774010"
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {
                "amount": "77751.04",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "to": "Счет 84163357546688983493"
        }]


def test_operations_sorted_len(five_elem_dict):
    assert len(funcs.operations_sorted((five_elem_dict))) == 5


def test_operation_sorted_max_year(five_elem_dict):
    assert funcs.operations_sorted((five_elem_dict))[0]["date"][:4] == "2019"


def test_operation_sorted_different_days():
    assert funcs.operations_sorted([{"date": "2019-07-03"}, {"date": "2019-07-04"}])[0]["date"][8:] == "04"


@pytest.fixture
def six_elem_dict():
    return [{
        "id": 649467725,
        "state": "EXECUTED",
        "date": "2018-04-14T19:35:28.978265",
        "operationAmount": {
            "amount": "96995.73",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 27248529432547658655",
        "to": "Счет 97584898735659638967"
    },
        {
            "id": 34148726,
            "state": "EXECUTED",
            "date": "2018-11-23T23:52:36.999661",
            "operationAmount": {
                "amount": "79428.73",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Platinum 5355133159258236",
            "to": "Maestro 8045769817179061"
        },
        {
            "id": 636137913,
            "state": "EXECUTED",
            "date": "2019-06-16T22:17:01.825020",
            "operationAmount": {
                "amount": "24260.78",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa Platinum 8990850370884895",
            "to": "Счет 15574304810835774010"
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {
                "amount": "79931.03",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215"
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {
                "amount": "77751.04",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "to": "Счет 84163357546688983493"
        },
        {
            "id": 594226727,
            "state": "EXECUTED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        },
    ]


def test_last_five_exec_ops(six_elem_dict):
    assert len(funcs.last_five_exec_ops(six_elem_dict)) == 5


@pytest.mark.parametrize("test_dict, date_expected", [
    ({
         "id": 649467725,
         "state": "EXECUTED",
         "date": "2018-04-14T19:35:28.978265",
         "operationAmount": {
             "amount": "96995.73",
             "currency": {
                 "name": "руб.",
                 "code": "RUB"
             }
         },
         "description": "Перевод организации",
         "from": "Счет 27248529432547658655",
         "to": "Счет 97584898735659638967"
     }, "14.04.2018"),
    ({
         "id": 34148726,
         "state": "EXECUTED",
         "date": "2018-11-23T23:52:36.999661",
         "operationAmount": {
             "amount": "79428.73",
             "currency": {
                 "name": "USD",
                 "code": "USD"
             }
         },
         "description": "Перевод с карты на карту",
         "from": "Visa Platinum 5355133159258236",
         "to": "Maestro 8045769817179061"
     }, "23.11.2018")
])
def test_correct_date(test_dict, date_expected):
    assert funcs.correct_date(test_dict) == date_expected


@pytest.mark.parametrize("test_dict, card_number_expected", [
    ({
         "id": 636137913,
         "state": "EXECUTED",
         "date": "2019-06-16T22:17:01.825020",
         "operationAmount": {
             "amount": "24260.78",
             "currency": {
                 "name": "USD",
                 "code": "USD"
             }
         },
         "description": "Перевод с карты на счет",
         "from": "Visa Platinum 8990850370884895",
         "to": "Счет 15574304810835774010"
     }, "Visa Platinum 8990 85** **** 4895"),
    ({
         "id": 615064591,
         "state": "CANCELED",
         "date": "2018-10-14T08:21:33.419441",
         "operationAmount": {
             "amount": "77751.04",
             "currency": {
                 "name": "руб.",
                 "code": "RUB"
             }
         },
         "description": "Перевод с карты на счет",
         "from": "Maestro 3928549031574026",
         "to": "Счет 84163357546688983493"
     }, "Maestro 3928 54** **** 4026")
])
def test_correct_card_info(test_dict, card_number_expected, key="from"):
    assert funcs.correct_card_info(test_dict[key]) == card_number_expected


@pytest.mark.parametrize("test_dict, expected_acc", [
    ({
         "id": 649467725,
         "state": "EXECUTED",
         "date": "2018-04-14T19:35:28.978265",
         "operationAmount": {
             "amount": "96995.73",
             "currency": {
                 "name": "руб.",
                 "code": "RUB"
             }
         },
         "description": "Перевод организации",
         "from": "Счет 27248529432547658655",
         "to": "Счет 97584898735659638967"
     }, "Счет **8967"),
    ({
         "id": 615064591,
         "state": "CANCELED",
         "date": "2018-10-14T08:21:33.419441",
         "operationAmount": {
             "amount": "77751.04",
             "currency": {
                 "name": "руб.",
                 "code": "RUB"
             }
         },
         "description": "Перевод с карты на счет",
         "from": "Maestro 3928549031574026",
         "to": "Счет 84163357546688983493"
     }, "Счет **3493")
])
def test_correct_bank_account(test_dict, expected_acc, key="to"):
    assert funcs.correct_bank_account(test_dict[key]) == expected_acc


@pytest.mark.parametrize("test_dict, expected", [
    ({
         "id": 587085106,
         "state": "EXECUTED",
         "date": "2018-03-23T10:45:06.972075",
         "operationAmount": {
             "amount": "48223.05",
             "currency": {
                 "name": "руб.",
                 "code": "RUB"
             }
         },
         "description": "Открытие вклада",
         "to": "Счет 41421565395219882431"
     }, "23.03.2018 Открытие вклада\nСчет **2431\n48223.05 руб.\n")
])
def test_create_acc_msg(test_dict, expected):
    assert funcs.create_acc_msg(test_dict) == expected


@pytest.mark.parametrize("test_dict, expected", [
    ({
         "id": 939719570,
         "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572",
         "operationAmount": {
             "amount": "9824.07",
             "currency": {
                 "name": "USD",
                 "code": "USD"
             }
         },
         "description": "Перевод организации",
         "from": "Счет 75106830613657916952",
         "to": "Счет 11776614605963066702"
     }, "30.06.2018 Перевод организации\nСчет **6952 -> Счет **6702\n9824.07 USD\n")
])
def test_from_acc_to_acc_msg(test_dict, expected):
    assert funcs.from_acc_to_acc_msg(test_dict) == expected


@pytest.mark.parametrize("test_dict, expected", [
    ({
         "id": 441945886,
         "state": "EXECUTED",
         "date": "2019-08-26T10:50:58.294041",
         "operationAmount": {
             "amount": "31957.58",
             "currency": {
                 "name": "руб.",
                 "code": "RUB"
             }
         },
         "description": "Перевод организации",
         "from": "Maestro 1596837868705199",
         "to": "Счет 64686473678894779589"
     }, "26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n")
])
def test_from_card_to_acc_msg(test_dict, expected):
    assert funcs.from_card_to_acc_msg(test_dict) == expected


@pytest.mark.parametrize("test_dict, expected", [
    ({
         "id": 34148726,
         "state": "EXECUTED",
         "date": "2018-11-23T23:52:36.999661",
         "operationAmount": {
             "amount": "79428.73",
             "currency": {
                 "name": "USD",
                 "code": "USD"
             }
         },
         "description": "Перевод с карты на карту",
         "from": "Visa Platinum 5355133159258236",
         "to": "Maestro 8045769817179061"
     },
     "23.11.2018 Перевод с карты на карту\nVisa Platinum 5355 13** **** 8236 -> Maestro 8045 76** **** 9061\n79428.73 USD\n")
])
def test_from_card_to_card_msg(test_dict, expected):
    assert funcs.from_card_to_card_msg(test_dict) == expected


def test_correct_card_name():
    assert funcs.correct_card_name({"from": "Visa 35434322"}["from"]) == ("Visa ", 5)
