import pytest
from gendiff.diff import generate_diff

FIXTURES_DIR = "tests/fixtures/"

@pytest.fixture
def json_file1():
    return f"{FIXTURES_DIR}file1.json"

@pytest.fixture
def json_file2():
    return f"{FIXTURES_DIR}file2.json"

@pytest.fixture
def yaml_file1():
    return f"{FIXTURES_DIR}file1.yaml"

@pytest.fixture
def yaml_file2():
    return f"{FIXTURES_DIR}file2.yaml"

@pytest.fixture
def expected_json_diff():
    with open(f"{FIXTURES_DIR}expected_json_diff.txt", "r") as file:
        return file.read()

@pytest.fixture
def expected_yaml_diff():
    with open(f"{FIXTURES_DIR}expected_yaml_diff.txt", "r") as file:
        return file.read()

def test_generate_diff_json(json_file1, json_file2, expected_json_diff):
    result = generate_diff(json_file1, json_file2)
    assert result == expected_json_diff

def test_generate_diff_yaml(yaml_file1, yaml_file2, expected_yaml_diff):
    result = generate_diff(yaml_file1, yaml_file2)
    assert result == expected_yaml_diff
