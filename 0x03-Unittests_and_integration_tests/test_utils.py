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

    @parameterized.expand([
        ({'a': 1}, ('b',), 'KeyError'),
        ({'a': {'b': 2}}, ('a', 'c'), 'KeyError')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_err):
        """Use the assertRaises context manager to test a KeyError"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
            self.assertEqual(expected_err, e.exception, f"""Should be equal
                                    to KeyError""")


"""
    objective:
    1- Define the TestGetJson(unittest.TestCase) class and implement the
        TestGetJson.test_get_json method to test that utils.get_json
        returns the expected result.
    2- Use unittest.mock.patch to patch requests.get. returns a Mock object
        with a json method that returns test_payload which you parametrize
        alongside the test_url that you will pass to get_json
    3- Test that the mocked get method was called exactly once (per input)
        with test_url as argument.
    4- Test that the output of get_json is equal to test_payload.
"""


class TestGetJson(unittest.TestCase):
    """Test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json"""
        fake_json = Mock()
        fake_json.json.return_value = test_payload
        with patch('requests.get') as mock:
            mock.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload, f'''Should be
                             equal to test_payload''')
            mock.assert_called_once_with(test_url)


"""
    objective:
    1- Define the TestMemoize(unittest.TestCase) class and implement the
        TestMemoize.test_memoize method, define the following:
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
    2- Use unittest.mock.patch to mock a_method. Test that when calling
        a_property twice, the correct result is returned but a_method is only
        called once using assert_called_once.
"""


class TestMemoize(unittest.TestCase):
    """Test memoize"""
    def test_memoize(self):
        """Test memoize"""
        class TestClass:
            """Test class"""
            def a_method(self):
                """a_method"""
                return 42

            @memoize
            def a_property(self):
                """a_property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            mock.return_value = 42
            test = TestClass()
            test.a_property
            test.a_property
            mock.assert_called_once()
