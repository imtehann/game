import requests, json, os, sys

token = os.getenv('GITHUB_TOKEN')
if not token:
    print('Error: GITHUB_TOKEN env var not set')
    sys.exit(1)

repo_data = {
    "name": "chess_famous_games",
    "private": False
}

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

resp = requests.post('https://api.github.com/user/repos', headers=headers, json=repo_data)
if resp.status_code == 201:
    print('Repository created successfully')
    repo_info = resp.json()
    print('Clone URL:', repo_info['clone_url'])
else:
    print('Failed to create repo', resp.status_code, resp.text)
    sys.exit(1)
