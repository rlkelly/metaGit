#!/bin/bash
set -e

alias home="cd"
alias metaGit="cd /metaGit"

for var in "$@"
do
    curl 'http://52.3.253.34/occm/api/vsa/volumes/VsaWorkingEnvironment-CASrF978/svm_First_Instance/first_instance/clone' -H 'Origin: http://52.3.253.34' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'Referer: http://52.3.253.34/occm/api-doc/' -H 'Cookie: JSESSIONID=1gnm17xx03t1y1qkekk3s4x8fv' -H 'Connection: keep-alive' --data-binary '{"newVolumeName": "'"$var"'"}' --compressed
    home
    metaGit
    sudo mount -o nolock  172.31.44.3:/$var /home/ec2-user/metaGit
    git checkout $var
    sudo umount /home/ec2-user/metaGit
done
