# access github repo

import os
import requests
import json


rv = requests.get('https://api.github.com/repos/rlkelly/metaGit?client_id=d501ec761e2427f67ccc&client_secret={}'.format(os.environ['client_secret']))
repo_information = json.loads(rv.text)
ssh_for_branch = repo_information['ssh_url']

# branches
rv = requests.get('https://api.github.com/repos/rlkelly/metaGit/branches?client_id=d501ec761e2427f67ccc&client_secret={}'.format(os.environ['client_secret']))
repo_branches = json.loads(rv.text)

