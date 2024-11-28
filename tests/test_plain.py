import pytest
from gendiff.formatters.plain import format_plain

def test_plain_formatter():
    diff = [
            {
                'key': 'common',
                'type': 'nested',
                'children': [
                    {'key': 'setting2', 'type': 'removed'},
                    {
                        'key': 'setting6',
                        'type': 'nested',
                        'children': [
                            {
                                'key': 'doge',
                                'type': 'nested',
                                'children': [
                                    {
                                        'key': 'wow',
                                        'type': 'changed',
                                        'old_value': '',
                                        'new_value': 'so much',
                                },
                            ],
                        },
                    ],
                },
            ],
        }
    ]
    expected = (
        "Property 'common.setting2' was removed\n"
        "Property 'common.setting6.doge.wow' was updated. From '' to 'so much'"
    )
    assert format_plain(diff) == expected
