#!/usr/bin/env python3
"""import files"""
import unittest
from unittest.mock import PropertyMock, patch
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD

"""
   objectives:
   1- declare the TestGithubOrgClient(unittest.TestCase) class and implement
      the test_org method.
   2- method should test that GithubOrgClient.org returns the correct value.
   3- Use @patch as a decorator to make sure get_json is called once with the
      expected argument but make sure it is not executed.
   4- Use @parameterized.expand as a decorator to parametrize the test with a
      couple of org examples to pass to GithubOrgClient, in this order:
        . google
        . abc
"""


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test_org method"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )
    """
        return a known payload. Test that the result of _public_repos_url is
        the expected one based on the mocked payload.
    """
    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, org_name, mock_get_json):
        """test_public_repos_url method"""
        with patch('client.GithubOrgClient.org', PropertyMock(
                        return_value=mock_get_json)):
            test_class = GithubOrgClient(org_name)._public_repos_url
            res = mock_get_json.get('repos_url')
            self.assertEqual(test_class, res, """public_repos_url matches the
                                                value of repos_url""")

    """
        Implement TestGithubOrgClient.test_has_license to unit-test
    """
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key):
        """test_has_license method"""
        test_class = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(test_class, True)

def requests_get(*args, **kwargs):
    """
        Function that mocks requests.get function
        Returns the correct json data based on the given input url
    """
    class MockResponse:
        """
            Mock response
        """
        def __init__(self, json_data):
            """
                Constructor method
            """
            self.json_data = json_data

        def json(self):
            """
                json method
            """
            return self.json_data

    if args[0] == 'https://api.github.com/orgs/google':
        return MockResponse(TEST_PAYLOAD[0][0])
    if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResponse(TEST_PAYLOAD[0][1])
