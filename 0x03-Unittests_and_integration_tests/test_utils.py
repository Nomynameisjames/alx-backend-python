#!/usr/bin/env python3
"""
    Test utils
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock

"""
    objective:
    1- write the first unit test for utils.access_nested_map.
    2- Create a TestAccessNestedMap class that inherits from unittest.TestCase.
    3-Implement the TestAccessNestedMap.test_access_nested_map method to test
        that the method returns what it is supposed to.
    4-Decorate the method with @parameterized.expand to test the function for
        following inputs:
    5-for each of these inputs, test with assertEqual that the function returns
        the expected result.
    6-The body of the test method should not be longer than 2 lines.
"""


class TestAccessNestedMap(unittest.TestCase):
    """
    Test access_nested_map
    """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected,
                         'Should be equal')
