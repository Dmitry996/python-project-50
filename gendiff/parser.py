import json
import yaml
from pathlib import Path


def open_file(file_path):
    suffix = Path(file_path).suffix

    with open(file_path) as file:
        if suffix == '.json':
            return json.loads(file.read())
        return yaml.safe_load(file.read())
