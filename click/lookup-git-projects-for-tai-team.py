import click
import requests


@click.command()
@click.option('--tai-team')
def get_git_projects(tai_team):

    repo_api_url = f"https://api.github.com/users/{tai_team}/repos"
    response = requests.get(repo_api_url)
    data = response.json()

    list_repo_names = [repo["name"] for repo in data]
    click.echo(list_repo_names)


if __name__ == "__main__":
    get_git_projects()
