import json

from typing import Any, Dict


def parse_json(filepath: str) -> Dict[str, Any]:
    with open(filepath, 'r') as file:
        return json.load(file)
