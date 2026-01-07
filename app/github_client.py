import requests
from app.config import settings

def fetch_repo(owner: str, repo: str):
    response = requests.get(
        f"{settings.GITHUB_API_URL}/repos/{owner}/{repo}",
        timeout=5
    )

    if response.status_code != 200:
        return None

    data = response.json()
    return {
        "name": data["name"],
        "owner": data["owner"]["login"],
        "stars": data["stargazers_count"],
        "url": data["html_url"]
    }
