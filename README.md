# metaGit

metaGit allows a user to integrate NetApp's Cloud ONTAP and Cloud Manager API to github.  Users can access all branches of a repository inside the repository itself, and only use a fraction of the space.  This is because metaGit uses the Cloud ONTAP cloning paradigm to only have lines of code that are consistent through all repositories saved once.

In order to run metaCloud, you need to create an account, update the ip address and api keys with your own information, and run populate.sh.

metaGit commands are: onTap <repository> to tap into a branch
                      closeTap <repository> to close a branch
