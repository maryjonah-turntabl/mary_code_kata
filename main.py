import requests


def get_public_github_repo_names():

    git_username = "maryjonah"
    repo_api_url = f"https://api.github.com/users/{git_username}/repos"

    response = requests.get(repo_api_url)
    data = response.json()

    list_repo_names = [repo["name"] for repo in data]

    return list_repo_names


print(get_public_github_repo_names())


