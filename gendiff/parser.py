import json

from typing import Any, Dict


def parse_json(data: str) -> Dict[str, Any]:
    return json.loads(data)
