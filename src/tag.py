import os
from git import GitCommandError

def create_tag(repo, branch, name):
    print("Craeted release tag {} pointing to {} branch".format(name, branch.name))

    try:
        tag = repo.create_tag(
            name, 
            ref=branch, 
            message="Release tag {} pointing to {} branch".format(name, branch.name)
        )
        return tag
    except GitCommandError:
        print("Git error when creating tag, does tag already exist?")