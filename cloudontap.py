# cloud on tap


rv = requests.get(url='http://52.3.253.34:80/occm/api/vsa/volumes?workingEnvironmentId=VsaWorkingEnvironment-CASrF978',
                  headers={'Cookie': 'JSESSIONID=1gnm17xx03t1y1qkekk3s4x8fv'})



{
  "workingEnvironmentId": "VsaWorkingEnvironment-CASrF978",
  "svmName": "svm_First_Instance",
  "aggregateName": "aggr1",
  "name": "newInstance",
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
    "shareName": "",
    "accessControl": {
      "permission": "default",
      "users": [
        ""
      ]
    }
  },
  "enableThinProvisioning": "boolean",
  "enableCompression": "boolean",
  "enableDeduplication": "boolean",
  "maxNumOfDisksApprovedToAdd": "integer"
}


{
    "name": "text",
    "svmName": "svm_First_Instance",
    "size": {
      "size": 100,
      "unit": "GB"
    },
    "usedSize": {
      "size": 0.00026702880859375,
      "unit": "GB"
    },
    "junctionPath": "/text",
    "compressionSpaceSaved": {
      "size": 0,
      "unit": "GB"
    },
    "deduplicationSpaceSaved": {
      "size": 0,
      "unit": "GB"
    },
    "thinProvisioning": true,
    "compression": false,
    "deduplication": true,
    "snapshotPolicy": "default",
    "securityStyle": "unix",
    "exportPolicyInfo": {
      "name": "export-svm_First_Instance-first_instance",
      "policyType": "custom",
      "ips": [
        "172.31.0.0/16"
      ]
    },
    "shareNames": [],
    "shareInfo": [],
    "parentVolumeName": "first_instance",
    "rootVolume": false,
    "state": "online",
    "volumeType": "rw",
    "aggregateName": "aggr1",
    "parentSnapshot": "clone_text.0",
    "autoSizeMode": "grow",
    "maxGrowSize": {
      "size": 1100,
      "unit": "GB"
    }