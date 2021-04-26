from git import Repo as GitRepo
from git import GitCommandError

def create_branch(repo, name):
    print("Created branch {} and checked out".format(name))

    try:
        new_branch = repo.create_head(name)
        new_branch.checkout()
        return new_branch
    except GitCommandError:
        print("Git error when creating tag, does branch already exist?")
