from helper import create_project, read_file_contents


def test_contains_configured_name_and_description(tmp_path):
    create_project(tmp_path, "foo", "This is a project")

    pyproject_toml_contents = read_file_contents(tmp_path, "foo/pyproject.toml")

    assert 'name = "foo"' in pyproject_toml_contents
    assert 'description = "This is a project"' in pyproject_toml_contents


def test_requires_minimum_python_version(tmp_path):
    create_project(tmp_path, "foo", "This is a project")

    pyproject_toml_contents = read_file_contents(tmp_path, "foo/pyproject.toml")

    assert 'python = "^3.11"' in pyproject_toml_contents


def test_contains_common_packages(tmp_path):
    create_project(tmp_path, "foo", "This is a project")

    pyproject_toml_contents = read_file_contents(tmp_path, "foo/pyproject.toml")

    assert 'numpy = "*"' in pyproject_toml_contents
    assert 'matplotlib = "*"' in pyproject_toml_contents
    assert 'pandas = "*"' in pyproject_toml_contents
    assert 'jupyter = "*"' in pyproject_toml_contents
