import os
import shutil
from dotenv import load_dotenv

from src.repo import clone_repo
from src.branch import create_branch
from src.tag import create_tag
from src.remote import get_remote, push


TEMP_FOLDER_PATH="./temp"
VERSION = "0.0.3"
REPOS = [
    { 
        'name': 'test-repo',
        'link': 'https://github.com/alejandro-santos-longboat/test-repo.git',
        'branch': 'main'
    }
]

def create_temp_folder():
    remove_temp_folder()
    os.mkdir(TEMP_FOLDER_PATH)

def remove_temp_folder():
    if os.path.exists(TEMP_FOLDER_PATH) and os.path.isdir(TEMP_FOLDER_PATH):
        shutil.rmtree(TEMP_FOLDER_PATH)

def cleanup():
    remove_temp_folder()

if __name__ == "__main__":
    load_dotenv()

    # Clone repos
    repos = [clone_repo(repo['link'], repo['name'], repo['branch']) for repo in REPOS]

    # Create branches
    branches = [(repo, create_branch(repo, f'Release_v{VERSION}')) for repo in repos]

    # Create tags
    tags = [create_tag(repo, branch, f'v{VERSION}') for (repo, branch) in branches]

    # Push to origin
    for (repo, branch) in branches:
        origin = get_remote(repo)
        if origin:
            push(repo, origin, tags)
        else:
            print(f"No origin found for repo {repo.name}")

    cleanup()


