from src.generators  import filter_by_currency, transaction_descriptions, card_number_generator

transactions = [
    {
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
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
]

def test_filter_by_currency():
    usd_transactions = list(filter_by_currency(transactions, "USD"))
    assert len(usd_transactions) == 2
    assert usd_transactions[0]['description'] == "Перевод организации"

    empty_transactions = list(filter_by_currency(transactions, "EUR"))
    assert len(empty_transactions) == 0

    empty_list_transactions = list(filter_by_currency([], "USD"))
    assert len(empty_list_transactions) == 0

def test_transaction_descriptions():
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == 2
    assert descriptions[0] == "Перевод организации"

    empty_descriptions = list(transaction_descriptions([]))
    assert len(empty_descriptions) == 0

def test_card_number_generator():
    card_numbers = list(card_number_generator(1, 5))
    assert card_numbers == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]

    card_numbers_range = list(card_number_generator(9999, 10000))
    assert card_numbers_range == ["0000 0000 0000 9999", "0000 0000 0001 0000"]
