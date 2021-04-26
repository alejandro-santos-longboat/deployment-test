import os
import shutil
from git import Repo as GitRepo
from src.errors import RepoIsEmptyError, RepoNotFoundError

TEMP_FOLDER_PATH="./temp"

def print_repository_info(repo):
    print('\tRepository description: {}'.format(repo.description))
    print('\tRepository active branch is {}'.format(repo.active_branch))
    print("\tLast commit for repository is {} - \"{}\" by {} at {}".format(
        str(repo.head.commit.hexsha), 
        repo.head.commit.summary, 
        repo.head.commit.author.name, 
        str(repo.head.commit.authored_datetime)
    ))

def clone_repo(repo_url, repo_name, branch = 'master'):
    local_path = os.path.join(TEMP_FOLDER_PATH, repo_name)
    if os.path.exists(local_path) and os.path.isdir(local_path):
        shutil.rmtree(local_path)

    cloned_repo = GitRepo.clone_from(
        repo_url, 
        os.path.join(TEMP_FOLDER_PATH, repo_name), 
        branch=branch
    )

    if cloned_repo.__class__ is not GitRepo:
        raise RepoNotFoundError
    assert os.path.isdir(cloned_repo.working_tree_dir) 

    print('Repo at {} successfully cloned.'.format(local_path))
    print_repository_info(cloned_repo)
    return cloned_repo