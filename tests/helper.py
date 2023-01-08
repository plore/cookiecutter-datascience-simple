from pathlib import Path

from cookiecutter.main import cookiecutter

TEMPLATE_DIR = str(Path(__file__).parent.parent)


def create_project(
    output_dir: Path,
    author: str | None = None,
    email: str | None = None,
    project_name: str = "foo",
    description: str = "A description",
) -> None:
    cookiecutter(
        template=TEMPLATE_DIR,
        output_dir=output_dir,
        no_input=True,
        extra_context={
            "full_name": author,
            "email": email,
            "project_name": project_name,
            "project_description": description,
        },
    )


def read_file_contents(base_directory: Path, relative_filepath: str) -> str:
    with open(base_directory.joinpath(Path(relative_filepath))) as created_file:
        return created_file.read()
