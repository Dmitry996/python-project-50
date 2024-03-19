import json
import yaml
from pathlib import Path


def get_data(file_path):
    """
    The function determines the file type and returns
    the read file data in dictionary format.
    for formats other than json and yaml(yml),
    returns a ValueError exception.
    Args:
        file_path: Path to file
    """
    suffix = Path(file_path).suffix

    with open(file_path) as file:
        match suffix:
            case '.json':
                return json.loads(file.read())
            case '.yaml' | '.yml':
                return yaml.safe_load(file.read())

        return ValueError('unsupported format file')
