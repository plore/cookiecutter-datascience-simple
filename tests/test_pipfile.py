from helper import create_project, read_file_contents


def test_pipfile_contains_common_packages(tmp_path):
    create_project(tmp_path, "foo", "This is a project")

    pipfile_contents = read_file_contents(tmp_path, "foo/Pipfile")

    assert 'numpy = "*"' in pipfile_contents
    assert 'matplotlib = "*"' in pipfile_contents
    assert 'pandas = "*"' in pipfile_contents
    assert 'jupyter = "*"' in pipfile_contents
