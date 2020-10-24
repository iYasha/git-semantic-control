from git import Repo
import git.objects.commit as goc
from typing import *
from git.exc import InvalidGitRepositoryError
from output_formatters import ExceptionFormatter
import re

VERSION_TEMPLATE = 'v$major.$minor.$patch*$message'


class GCV:

    def __init__(self, path: str, message: str, *, version: Optional[str] = None):
        try:
            self.repository = Repo(path)
        except InvalidGitRepositoryError:
            ExceptionFormatter.format(f'Repository not found in path: {path}',
                                      'Please, try in another folder with .git')
        self.message = message
        self.version = version if version is not None else self._get_version_

    @property
    def get_last_commit(self) -> Optional[goc.Commit]:
        return next(self.repository.iter_commits())

    @property
    def _get_version_(self) -> str:
        commit = self.get_last_commit
        if commit is not None:
            pattern = re.escape(VERSION_TEMPLATE)
            pattern = re.sub(r'\\\$(\w+)', r'(?P<\1>.*)', pattern)
            match = re.match(pattern, commit.message)
            if match is not None:
                return f'v{match.group("major").strip()}.{match.group("minor").strip()}.{match.group("patch").strip()}'
        return 'v0.1.0'

    @property
    def version(self):
        return self.version

    def commit(self):
        pass
