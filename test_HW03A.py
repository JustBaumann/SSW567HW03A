import unittest
from unittest.mock import patch
import requests
from HW03A import get_user_repos_and_commits


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError


class TestGitHubApi(unittest.TestCase):
    @patch('requests.get')
    def test_user_with_repos(self, mock_get):
        # First mock: repo list
        # Second mock: commit list
        mock_get.side_effect = [
            MockResponse([{"name": "test-repo"}], 200),
            MockResponse([{"sha": "abc123"}, {"sha": "def456"}], 200)
        ]
        result = get_user_repos_and_commits("fakeuser")
        self.assertEqual(result, [("test-repo", 2)])

    @patch('requests.get')
    def test_user_not_found(self, mock_get):
        mock_get.return_value = MockResponse({"message": "Not Found"}, 404)
        with self.assertRaises(requests.exceptions.HTTPError):
            get_user_repos_and_commits("nouser")


if __name__ == "__main__":
    unittest.main()
