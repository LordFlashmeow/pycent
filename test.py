import unittest

import pycent


class TestPycent(unittest.TestCase):

    def setUp(self):
        self.pycent = pycent.pycent()

    def test_we_get_the_percentage_of_a_number(self):
        """
        Tests our pycent.percent_of method.

        test_cases is a data provider in the format of
        [
            [percentage_of, number, expected_result]
        ]

        i.e.
        [
            [5, 20, 1]
        ]
        """

        test_cases = [
            [5, 20, 1],
            [100, 100, 100],
            [75, 3, 2.25]
        ]

        for test_case in test_cases:

            percent_of = test_case[0]
            number = test_case[1]
            expected_result = test_case[2]

            self.assertEqual(self.pycent.percent_of(percent_of, number), expected_result)

    def test_we_calculate_the_percentage_of_a_number_given_a_part_and_whole(self):
        """
        Tests our pycent.percentage method.

        test_cases is a data provider in the format of
        [
            [part, whole, expected_result]
        ]

        i.e.
        [
            10, 25, 40]
        ]
        """

        test_cases = [
            [10, 25, 40],
        ]

        for test_case in test_cases:

            percent_of = test_case[0]
            number = test_case[1]
            expected_result = test_case[2]

            self.assertEqual(self.pycent.percentage(percent_of, number), expected_result)






