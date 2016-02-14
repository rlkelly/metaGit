#access github repo

import os
import requests
import json
import sys

def get_branches():

    os.environ['client_secret'] = '1fe396b7960ca225804f8929855b4853467f723a'

    rv = requests.get('https://api.github.com/repos/rlkelly/metaGit?client_id=da4a8820b2a3bb2ad7ac&client_secret={}'.format(os.environ['client_secret']))
    repo_information = json.loads(rv.text)
    ssh_for_branch = repo_information['ssh_url']

    # branches
    rv = requests.get('https://api.github.com/repos/rlkelly/metaGit/branches?client_id=da4a8820b2a3bb2ad7ac&client_secret={}'.format(os.environ['client_secret']))
    repo_branches = json.loads(rv.text)

    branches = map(lambda x: str(x['name']), repo_branches)

    cookies = {
        'JSESSIONID': '1gnm17xx03t1y1qkekk3s4x8fv',
    }

    headers = {
        'Origin': 'http://52.3.253.34',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Referer': 'http://52.3.253.34/occm/api-doc/',
        'Connection': 'keep-alive',
        'Content-Length': '0',
    }

    for branch in branches:
        requests.delete('http://52.3.253.34/occm/api/vsa/volumes/VsaWorkingEnvironment-CASrF978/svm_First_Instance/{}'.format(branch), headers=headers, cookies=cookies)

    try:
        main = branches.pop(branches.index(sys.argv[1]))
    except IndexError:
        main = branches.pop(branch.index('master'))

    order = main + ' ' + ' '.join(branches)

    print branches

    return branches

get_branches()