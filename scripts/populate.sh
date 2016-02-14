#!/bin/bash
set -e

sh create_master.sh

OUTPUT2="$(python get_branches.py)"
FINAL="$(sh repo_tree.sh ${OUTPUT2})"
