import requests


class GitService:
    def __init__(self):
        pass

    def get_git_repos_for_org(self, org):

        repo_api_url = f"https://api.github.com/users/{org}/repos"

        response = requests.get(repo_api_url)
        data = response.json()

        list_repo_names = [repo["name"] for repo in data]

        return list_repo_names


class GitGateway:
    pass


# obj_git_service = GitService()
# print(obj_git_service.get_git_repos_for_org("maryjonah"))

