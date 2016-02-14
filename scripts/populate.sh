#!/bin/bash
set -e

rm -rf /home/ec2-user/metaGit/branches

sh create_master.sh

sleep 5

OUTPUT2=$(python get_branches.py)
FINAL="$(sh repo_tree.sh ${OUTPUT2})"

