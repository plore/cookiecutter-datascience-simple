import pytest
from helper import create_project, read_file_contents


def test_contains_configured_project_name_author_email_and_description(tmp_path):
    create_project(
        tmp_path,
        author="Jane Doe",
        email="jane.doe@example.com",
        project_name="bar",
        description="This is a project",
    )

    pyproject_toml_contents = read_file_contents(tmp_path, "bar/pyproject.toml")

    assert 'name = "bar"' in pyproject_toml_contents
    assert 'authors = ["Jane Doe <jane.doe@example.com>"]' in pyproject_toml_contents
    assert 'description = "This is a project"' in pyproject_toml_contents


@pytest.mark.parametrize(
    "author,email,result",
    [
        ("Jane Doe", "jane.doe@example.com", '["Jane Doe <jane.doe@example.com>"]'),
        ("Jane Doe", None, '["Jane Doe"]'),
        (None, "jane.doe@example.com", '["<jane.doe@example.com>"]'),
        (None, None, "[]"),
    ],
)
def test_author_and_email_are_optional(tmp_path, author, email, result):
    create_project(tmp_path, author=author, email=email, project_name="bar")

    pyproject_toml_contents = read_file_contents(tmp_path, "bar/pyproject.toml")

    assert f"authors = {result}" in pyproject_toml_contents


def test_requires_minimum_python_version(tmp_path):
    create_project(tmp_path)

    pyproject_toml_contents = read_file_contents(tmp_path, "foo/pyproject.toml")

    assert 'python = "^3.11"' in pyproject_toml_contents


def test_contains_common_packages(tmp_path):
    create_project(tmp_path)

    pyproject_toml_contents = read_file_contents(tmp_path, "foo/pyproject.toml")

    assert 'numpy = "*"' in pyproject_toml_contents
    assert 'matplotlib = "*"' in pyproject_toml_contents
    assert 'pandas = "*"' in pyproject_toml_contents
    assert 'jupyter = "*"' in pyproject_toml_contents
