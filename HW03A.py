import requests

def get_user_repos_and_commits(username):
    repos_url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(repos_url)
    repos_response.raise_for_status()
    repos_data = repos_response.json()
    results = []

    for repo in repos_data:
        repo_name = repo.get("name")
        commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
        commits_response = requests.get(commits_url)
        commits_response.raise_for_status()
        commits_data = commits_response.json()
        results.append((repo_name, len(commits_data)))

    return results
if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    results = get_user_repos_and_commits(username)
    for repo, commits in results:
        print(f"Repo: {repo} Number of commits: {commits}")
