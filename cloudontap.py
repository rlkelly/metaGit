# cloud on tap


rv = requests.get(url='http://52.3.253.34:80/occm/api/vsa/volumes?workingEnvironmentId=VsaWorkingEnvironment-CASrF978',
                  headers={'Cookie': 'JSESSIONID=1gnm17xx03t1y1qkekk3s4x8fv'})



{
  "workingEnvironmentId": "VsaWorkingEnvironment-CASrF978",
  "svmName": "svm_First_Instance",
  "aggregateName": "aggr1",
  "name": "newInstance2",
  "size": {
    "size": "100",
    "unit": "GB"
  },
  "initialSize": {
    "size": "1",
    "unit": "GB"
  },
  "snapshotPolicyName": "default",
  "exportPolicyInfo": {
    "policyType": "custom",
    "ips": [
      "172.31.0.0/16"
    ]
  },
  "shareInfo": {
    "shareName": "newInstance2",
    "accessControl": {
      "permission": "full_control",
      "users": [
        "Robert Kelly"
      ]
    }
  },
  "enableThinProvisioning": true,
  "enableCompression": false,
  "enableDeduplication": true,
  "maxNumOfDisksApprovedToAdd": 1
}



curl 'http://52.3.253.34/occm/api/vsa/volumes/VsaWorkingEnvironment-CASrF978/svm_First_Instance/first_instance/clone' -H 'Origin: http://52.3.253.34' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Referer: http://52.3.253.34/occm/api-doc/' -H 'Cookie: JSESSIONID=1gnm17xx03t1y1qkekk3s4x8fv' -H 'Connection: keep-alive' --data-binary '{"newVolumeName": "New_One"}' --compressed
