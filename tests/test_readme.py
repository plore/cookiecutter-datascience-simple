from helper import create_project, read_file_contents


def test_readme_contains_project_name_and_description(tmp_path):
    create_project(tmp_path, project_name="foo", description="This is a project")

    readme_contents = read_file_contents(tmp_path, "foo/README.md")

    assert "# foo" in readme_contents
    assert "This is a project" in readme_contents
