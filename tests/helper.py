from pathlib import Path

from cookiecutter.main import cookiecutter

TEMPLATE_DIR = str(Path(__file__).parent.parent)


def create_project(output_dir: Path, name: str, description: str) -> None:
    cookiecutter(
        template=TEMPLATE_DIR,
        output_dir=output_dir,
        no_input=True,
        extra_context={
            "project_name": name,
            "project_description": description,
        },
    )


def read_file_contents(base_directory: Path, relative_filepath: str) -> str:
    with open(base_directory.joinpath(Path(relative_filepath))) as created_file:
        return created_file.read()
