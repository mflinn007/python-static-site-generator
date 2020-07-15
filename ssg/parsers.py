import shutil

from typing import List
from pathlib import Path


class Parser:

    extensions: List[str] = []

    def valid_extensions(self, extensions):
        return extensions in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        """To be implemented by a sub class"""
        raise NotImplementedError

    def read(self, path):
        """using a context manager, read a file"""
        with open(path, 'r') as file:
            return file.read()

    def write(self, path, dest, content, ext=".html"):
        """using a context manager, write to a file"""
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)

    def copy(self, path, source, dest):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = ['.jpg', '.png', '.git', '.css', '.html']

    def parse(self, path, source, dest):
        self.copy(path, source, dest)
