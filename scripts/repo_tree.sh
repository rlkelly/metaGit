#!/bin/bash
alias home="cd"
alias metaGit="cd metaGit"

curl 'http://52.3.253.34/occm/api/vsa/volumes?createAggregateIfNotFound=false' -H 'Origin: http://52.3.253.34' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Referer: http://52.3.253.34/occm/api-doc/' -H 'Cookie: JSESSIONID=1gnm17xx03t1y1qkekk3s4x8fv' -H 'Connection: keep-alive' --data-binary $'{\n  "workingEnvironmentId": "VsaWorkingEnvironment-CASrF978",\n  "svmName": "svm_First_Instance",\n  "aggregateName": "aggr1",\n  "name": "'"$1"'",\n  "size": {\n    "size": "10",\n    "unit": "GB"\n  },\n  "initialSize": {\n    "size": "1",\n    "unit": "GB"\n  },\n  "snapshotPolicyName": "default",\n  "exportPolicyInfo": {\n    "policyType": "custom",\n    "ips": [\n      "172.31.0.0/16"\n    ]\n  },\n  \n  "enableThinProvisioning": true,\n  "enableCompression": false,\n  "enableDeduplication": true,\n  "maxNumOfDisksApprovedToAdd": 1\n}' --compressed

for var in "${@: 2:999999}"
do
    eval "ssh-agent -s"
    eval ssh-add ~/.ssh/github
    curl "http://52.3.253.34/occm/api/vsa/volumes/VsaWorkingEnvironment-CASrF978/svm_First_Instance/$1/clone" -H 'Origin: http://52.3.253.34' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Referer: http://52.3.253.34/occm/api-doc/' -H 'Cookie: JSESSIONID=1gnm17xx03t1y1qkekk3s4x8fv' -H 'Connection: keep-alive' --data-binary '{"newVolumeName": "'"$var"'"}' --compressed
    home
    sudo mount -o nolock  172.31.44.3:/$var /home/ec2-user/metaGit
    metaGit
    git checkout $var
    home
    sudo umount /home/ec2-user/metaGit
done
