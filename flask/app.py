from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/lookup-git-projects-for-tai-team/<nameOfTeam>')
def flask_function(nameOfTeam):

    repo_api_url = f"https://api.github.com/users/{nameOfTeam}/repos"
    response = requests.get(repo_api_url)
    data = response.json()

    list_repo_names = [repo["name"] for repo in data]
    return jsonify(list_repo_names)
