import unittest
from src.processing.processing import filter_by_state, sort_by_date


class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        self.data = [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        ]

    def test_filter_by_state(self):
        self.assertEqual(len(filter_by_state(self.data)), 2)
        self.assertEqual(len(filter_by_state(self.data, 'CANCELED')), 2)

    def test_sort_by_date(self):
        sorted_data = sort_by_date(self.data)
        self.assertEqual(sorted_data[0]['id'], 41428829)

    if __name__ == '__main__':
        unittest.main()


import pytest
from src.processing.processing import filter_by_state

def test_filter_by_state():
    example_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]

    # Проверка фильтрации по состоянию 'EXECUTED'
    executed_items = filter_by_state(example_data)
    assert executed_items == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]

    # Проверка фильтрации по состоянию 'CANCELED'
    canceled_items = filter_by_state(example_data, 'CANCELED')
    assert canceled_items == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
    ]

    # Проверка фильтрации по состоянию, которого нет в данных
    not_found_items = filter_by_state(example_data, 'PENDING')
    assert not found_items == []

    from src.processing.processing import sort_by_date  # Замените 'processing' на реальное имя вашего модуля

    def test_sort_by_date():
        example_data = [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        ]

        # Проверка сортировки по дате в порядке убывания
        sorted_data_desc = sort_by_date(example_data)
        assert sorted_data_desc == [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        ]

        # Проверка сортировки по дате в порядке возрастания
        sorted_data_asc = sort_by_date(example_data, reverse=False)
        assert sorted_data_asc == [
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        ]

        @pytest.mark.parametrize("input_data, expected_output", [
            ([
                 {'id': 1, 'state': 'EXECUTED'},
                 {'id': 2, 'state': 'CANCELED'},
             ], 'EXECUTED', [{'id': 1, 'state': 'EXECUTED'}]),
            ([
                 {'id': 1, 'state': 'CANCELED'},
                 {'id': 2, 'state': 'CANCELED'},
             ], 'CANCELED', [{'id': 1, 'state': 'CANCELED'}, {'id': 2, 'state': 'CANCELED'}]),
        ])
        def test_filter_by_state_parametrized(input_data, expected_output):
            assert filter_by_state(input_data) == expected_output
