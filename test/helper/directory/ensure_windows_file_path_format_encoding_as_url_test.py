import pytest

from browserist import helper


@pytest.mark.parametrize("path, expected", [
    ("file://path\\to\\file.html", "file://path/to/file.html"),
    ("file:///path\\to\\file.html", "file:///path/to/file.html"),
    ("file://C:path\\to\\file.html", "file:///C:path/to/file.html"),
    ("file:///C:path\\to\\file.html", "file:///C:path/to/file.html"),
])
def test_helper_directory_ensure_windows_file_path_format_encoding_as_url(path: str, expected: str) -> None:
    assert helper.directory.ensure_windows_file_path_format_encoding_as_url(path) == expected
