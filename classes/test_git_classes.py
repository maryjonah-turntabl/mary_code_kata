from unittest import mock
from classes.git_classes import GitService


@mock.patch("classes.git_classes.requests.get")
def test_get_git_repo_for_org(mock_request_get):
    obj_git_service = GitService()
    mock_request_get.return_value = mock.Mock(**{"status_code": 200, "json.return_value":
                                                 [
                                                     {"name": "repo1"},
                                                     {"name": "repo2"},
                                                     {"name": "repo3"},
                                                     {"name": "repo4"}
                                                 ]})
    assert obj_git_service.get_git_repos_for_org("turntabl") == ["repo1", "repo2", "repo3", "repo4"]
    mock_request_get.assert_called_once()
