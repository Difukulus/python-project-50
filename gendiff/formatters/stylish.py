def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        indent = "    " * (depth + 1)
        for key, val in value.items():
            lines.append(f"{indent}{key}: {format_value(val, depth + 1)}")
        return "{\n" + "\n".join(lines) + f"\n{'    ' * depth}}}"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    return str(value)

def stylish(diff, depth=0):
    result = []
    indent = "    " * depth
    for node in diff:
        key = node["key"]
        node_type = node["type"]
        if node_type == "added":
            result.append(f"{indent}  + {key}: {format_value(node['value'], depth)}")
        elif node_type == "removed":
            result.append(f"{indent}  - {key}: {format_value(node['value'], depth)}")
        elif node_type == "changed":
            result.append(f"{indent}  - {key}: {format_value(node['old_value'], depth)}")
            result.append(f"{indent}  + {key}: {format_value(node['new_value'], depth)}")
        elif node_type == "unchanged":
            result.append(f"{indent}    {key}: {format_value(node['value'], depth)}")
        elif node_type == "nested":
            result.append(f"{indent}    {key}: {{")
            result.append(stylish(node["children"], depth + 1))
            result.append(f"{indent}    }}")
    return "\n".join(result)

def format_stylish(diff):
    return "{\n" + stylish(diff) + "\n}"
