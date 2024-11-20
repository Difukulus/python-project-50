import json
from typing import Any, Dict


def generate_diff(file_path1: str, file_path2: str) -> str:
    with open(file_path1, 'r') as file1:
        data1 = json.load(file1)
    with open(file_path2, 'r') as file2:
        data2 = json.load(file2)
    all_keys = sorted(set(data1.keys()).union(data2.keys()))

    result = []
    for key in all_keys:
        if key in data1 and key not in data2:
            result.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            result.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            result.append(f"  - {key}: {data1[key]}")
            result.append(f"  + {key}: {data2[key]}")
        else:
            result.append(f"    {key}: {data1[key]}")
    return "{\n" + "\n".join(result) + "\n}"
