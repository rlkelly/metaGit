import subprocess

subprocess.call("sh create_master.sh", shell=True)
ans = subprocess.call("python get_branches.py", shell=True)
print ans
subprocess.call("sh repo_tree.sh {}".format(ans), shell=True)


