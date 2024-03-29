import os
import subprocess
from contextlib import nullcontext as does_not_raise
from pathlib import Path
from unittest.mock import patch

import nbformat
import pytest
from helper import create_project
from nbconvert.preprocessors import ExecutePreprocessor

PROJECT_NAME = "foo"


def create_and_run_notebook():
    notebook = nbformat.v4.new_notebook()
    notebook["cells"] = [nbformat.v4.new_code_cell("1+1")]

    ep = ExecutePreprocessor()
    ep.preprocess(notebook)

    path = Path(os.getcwd()) / "test_notebook.ipynb"
    with open(path, "w") as outfile:
        nbformat.write(notebook, outfile)


@pytest.fixture
def initialize_project(tmp_path_factory):
    parent_dir = tmp_path_factory.mktemp("parent")
    create_project(parent_dir, project_name=PROJECT_NAME)
    old_working_dir = os.getcwd()
    os.chdir(parent_dir / PROJECT_NAME)
    subprocess.run(["make", "init"], check=True)
    yield
    os.chdir(old_working_dir)


def test_format_target_finds_no_errors(initialize_project):
    with does_not_raise():
        subprocess.run(["make", "format"], check=True)


@patch.dict(
    os.environ, {"PYDEVD_DISABLE_FILE_VALIDATION": "1"}
)  # to disable debug messages
def test_format_corrects_notebooks_and_strips_output(initialize_project):
    create_and_run_notebook()

    subprocess.run(["make", "format"], check=True)

    with open("test_notebook.ipynb", "r") as notebook_file:
        notebook = nbformat.read(notebook_file, as_version=4)

    assert notebook["cells"][0]["source"] == "1 + 1"
    assert notebook["cells"][0]["outputs"] == []


def test_format_applies_formatting(initialize_project):
    with open("src/main.py", "w") as main_file:
        main_file.write("x=42")

    subprocess.run(["make", "format"], check=True)

    with open("src/main.py", "r") as main_file:
        assert main_file.readlines() == ["x = 42\n"]


def test_format_performs_import_sorting(initialize_project):
    with open("src/main.py", "w") as main_file:
        main_file.write("import sys\n")
        main_file.write("import os\n")

    subprocess.run(["make", "format"], check=True)

    with open("src/main.py", "r") as main_file:
        assert main_file.readlines() == ["import os\n", "import sys\n"]


def test_lint_target_finds_no_errors(initialize_project):
    with does_not_raise():
        subprocess.run(["make", "lint"], check=True)


@patch.dict(os.environ, {"PYDEVD_DISABLE_FILE_VALIDATION": "1"})
def test_can_run_notebooks(initialize_project):
    with does_not_raise():
        create_and_run_notebook()


@patch.dict(os.environ, {"PYDEVD_DISABLE_FILE_VALIDATION": "1"})
def test_pre_commit_hook_fails_on_dirty_notebook_and_cleans_output(initialize_project):
    create_and_run_notebook()

    subprocess.run(["git", "init"], check=True)
    subprocess.run(["pre-commit", "install"], check=True)
    subprocess.run(["git", "add", "test_notebook.ipynb"], check=True)
    result = subprocess.run(
        ["git", "commit", "-m", "'Add notebook'"], capture_output=True
    )

    assert result.returncode != 0
    assert "Failed" in str(result.stderr)
    assert "hook" in str(result.stderr)

    with open("test_notebook.ipynb", "r") as notebook_file:
        notebook = nbformat.read(notebook_file, as_version=4)
    assert notebook["cells"][0]["outputs"] == []

    subprocess.run(["git", "add", "test_notebook.ipynb"], check=True)
    result = subprocess.run(
        ["git", "commit", "-m", "'Add notebook'"], capture_output=True
    )
    assert result.returncode == 0
