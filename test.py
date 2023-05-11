""" Unit tests for autojohn """

import solicit


def test_query_index_file():
    """A high level end to end smoke test to see if I even get a response"""

    result = solicit.query_index_file("obsidian_index.json", "What are the three seashells?")
    assert isinstance(result, str)

    print(result)
