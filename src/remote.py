def get_remote(repo):
    return repo.remotes['origin']

def fetch(origin):
    if origin.exists():
        origin.fetch()

def push(repo, origin, tags):
    if origin.exists():
        for tag in tags:
            origin.push(tag)
        repo.git.push("--set-upstream", origin, repo.head.ref)