import pytest
from gendiff.diff import build_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.diff import generate_diff
from gendiff.formatters.plain import plain

def test_build_diff():
    data1 = {
        "common": {"setting1": "Value 1", "setting2": 200},
        "group1": {"baz": "bas", "foo": "bar"}
    }
    data2 = {
        "common": {"follow": False, "setting1": "Value 1"},
        "group1": {"baz": "bars", "foo": "bar"}
    }
    diff = build_diff(data1, data2)
    print(diff)
    assert diff is not None
    
def test_format_stylish():
    diff = [
        {"key": "common", "type": "nested", "children": [

            {"key": "follow", "type": "added", "value": False},
            {"key": "setting1", "type": "unchanged", "value": "Value 1"}
        ]}
    ]
    result = format_stylish(diff)
    print(result)
    assert result.startswith("{")

def test_generate_diff():
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    print(result)
    assert result is not None
    assert isinstance(result, str)

def test_plain_format():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    expected = (
        "Property 'common.follow' was added with value: false\n"
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting3' was updated. From true to null\n"
        "Property 'common.setting4' was added with value: 'blah blah'\n"
        "Property 'common.setting5' was added with value: [complex value]\n"
        "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'\n"
        "Property 'common.setting6.ops' was added with value: 'vops'\n"
        "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
        "Property 'group1.nest' was updated. From [complex value] to 'str'\n"
        "Property 'group2' was removed\n"
        "Property 'group3' was added with value: [complex value]"
    )
    assert generate_diff(file1, file2, 'plain') == expected
