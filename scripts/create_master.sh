
#!/bin/bash
alias home="cd"
alias metaGit="cd metaGit"
alias metaMaster="cd $1"

curl 'http://52.3.253.34/occm/api/vsa/volumes?createAggregateIfNotFound=false' -H 'Origin: http://52.3.253.34' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Referer: http://52.3.253.34/occm/api-doc/' -H 'Cookie: JSESSIONID=1gnm17xx03t1y1qkekk3s4x8fv' -H 'Connection: keep-alive' --data-binary $'{  "workingEnvironmentId": "VsaWorkingEnvironment-CASrF978",  "svmName": "svm_First_Instance",  "aggregateName": "aggr1",  "name": "master",  "size": {    "size": "10",    "unit": "GB"  },  "initialSize": {    "size": "1",    "unit": "GB"  },  "snapshotPolicyName": "default",  "exportPolicyInfo": {    "policyType": "custom",    "ips": [      "172.31.0.0/16"    ]  },    "enableThinProvisioning": true,  "enableCompression": false,  "enableDeduplication": true,  "maxNumOfDisksApprovedToAdd": 1}' --compressed

eval "ssh-agent -s"
eval ssh-add ~/.ssh/github
home
pwd
sudo mount -o nolock  172.31.44.3:/$1 /home/ec2-user/metaGit
metaGit
metaMaster
git clone git@github.com:rlkelly/metaGit.git
home
sudo umount /home/ec2-user/metaGit
