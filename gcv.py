from git import Repo
from typing import *
from git.exc import InvalidGitRepositoryError
from output_formatters import ExceptionFormatter


class GCV:

    def __init__(self, path: str, message: str, *, version: Optional[str] = None):
        try:
            self.repository = Repo(path)
        except InvalidGitRepositoryError:
            ExceptionFormatter.format(f'Repository not found in path: {path}', 'Please, try in another folder with .git')
        self.message = message
        self.version = version

    def get_version(self):
        pass

    def commit(self):
        pass


    # repo = Repo(path)
    # assert not repo.bare
    # for commit in repo.iter_commits():
    #     print(commit.message)
    #     print(commit.author)