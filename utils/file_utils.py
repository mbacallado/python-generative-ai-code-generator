import yaml

from officeparserpy import parse_office

def read_text_from_document(document_path):
    """Extract text content from a document."""

    with open(document_path, "rb") as document_file:
        document_bytes = document_file.read()

    return parse_office(document_bytes)


def write_to_file(output_directory, file_name, file_extension, content):
    """Write generated code to a file."""

    with open(
        f"{output_directory}{file_name}.{file_extension}",
        "w",
        encoding="utf-8"
    ) as output_file:
        output_file.write(content)


def read_yaml(file_name):
    """Load configuration data from a YAML file."""

    config_data = None

    with open(file_name, encoding="utf-8") as yaml_file:
        try:
            config_data = yaml.safe_load(yaml_file)

        except yaml.YAMLError as error:
            print(error)

    return config_data