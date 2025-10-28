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
