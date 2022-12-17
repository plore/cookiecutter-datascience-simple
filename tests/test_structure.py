import os
from pathlib import Path

from helper import create_project

TEMPLATE_DIR = str(Path(__file__).parent.parent)


def filepaths_from(top_directory: Path) -> list[Path]:
    paths = []
    for path, _, files in os.walk(top_directory):
        for file in files:
            paths.append(Path(path).joinpath(file).relative_to(top_directory))
    return paths


def test_has_expected_paths(tmp_path):
    create_project(tmp_path, "foo", "This is a project")

    created_paths = {str(path) for path in filepaths_from(tmp_path)}

    expected_paths = {
        "foo/.flake8",
        "foo/.gitignore",
        "foo/.pre-commit-config.yaml",
        "foo/.pylintrc",
        "foo/src/.gitkeep",
        "foo/Makefile",
        "foo/Pipfile",
        "foo/README.md",
    }
    assert expected_paths.issubset(created_paths)
