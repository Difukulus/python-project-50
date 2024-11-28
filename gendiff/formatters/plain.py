def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)

def plain(diff, parent_path=""):
    lines = []
    for node in diff:
        key = node['key']
        property_path = f"{parent_path}.{key}" if parent_path else key

        if node['type'] == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{property_path}' was added with value: {value}")
        elif node['type'] == 'removed':
            lines.append(f"Property '{property_path}' was removed")
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(f"Property '{property_path}' was updated. From {old_value} to {new_value}")
        elif node['type'] == 'nested':
            lines.extend(plain(node['children'], property_path))
    result = "\n".join(lines)
    return result

def format_plain(diff):
    return plain(diff)
