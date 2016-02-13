import os

# access github repo

rv = requests.get(url='http://52.3.253.34:80/occm/api/vsa/volumes?workingEnvironmentId=VsaWorkingEnvironment-CASrF978',
                  headers={'Cookie': 'JSESSIONID=1gnm17xx03t1y1qkekk3s4x8fv'})

curl 'https://api.github.com/repos/rlkelly/metaGit/branches?client_id=d501ec761e2427f67ccc&client_secret={}'.format(os.environ['client_secret'])