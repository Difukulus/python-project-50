from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain

def format_diff(diff, formatter="stylish"):
    if formatter == "stylish":
        return format_stylish(diff)
    if formatter == "plain":
        return format_plain(diff)
    raise ValueError(f"Unknown format: {formatter}")
