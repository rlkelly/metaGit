#!/bin/bash
alias home="cd"

home
sudo mount -o nolock  172.31.44.3:/$1 /home/ec2-user/metaGit/branches/$1

