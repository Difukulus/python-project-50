import pytest
from gendiff.diff import generate_diff

@pytest.fixture
def file_paths(tmp_path):
    file1 = tmp_path / "file1.json"
    file2 = tmp_path / "file2.json"
    file1.write_text('{"host": "hexlet.io", "timeout": 50}')
    file2.write_text('{"host": "hexlet.io", "timeout": 20, "verbose": true}')
    return str(file1), str(file2)

def test_generate_diff(file_paths):
    file1, file2 = file_paths
    expected = '''{
- timeout: 50
+ timeout: 20
+ verbose: true
}'''
    assert generate_diff(file1, file2) == expected
