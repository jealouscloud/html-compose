from html_compose.util_funcs import flatten_iterable, glob_matcher


def test_iterator_flatten():
    nested_list = [1, [2, [3, 4], 5], [6, [7, [8, 9]]]]
    assert list(flatten_iterable(nested_list)) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert list(flatten_iterable((x for x in nested_list))) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ]

    string_demo = [1, [2, [3, ["arst"]]]]
    assert list(flatten_iterable(string_demo)) == [1, 2, 3, "arst"]

    bytes_demo = [1, 2, 3, bytes([1, 2, 3, 4])]
    assert list(flatten_iterable(bytes_demo)) == [1, 2, 3, bytes([1, 2, 3, 4])]


def test_glob_func():
    test_cases = [
        # Basic matching
        ("file.txt", "file.txt", True),
        ("dir/file.txt", "dir/file.txt", True),
        # * as entire segment - matches one segment
        ("*/file.txt", "dir/file.txt", True),
        ("*/file.txt", "dir1/dir2/file.txt", False),
        # * as part of segment - matches any characters
        ("dir/file*.txt", "dir/file1.txt", True),
        ("dir/file*.txt", "dir/fileabc.txt", True),
        ("dir/*.txt", "dir/file.txt", True),
        # ** - matches any number of segments
        ("**/file.txt", "file.txt", True),
        ("./**/file.txt", "file.txt", True),
        ("**/file.txt", "dir/file.txt", True),
        ("**/file.txt", "dir1/dir2/file.txt", True),
        ("dir/**/file.txt", "dir/file.txt", True),
        ("dir/**/file.txt", "dir/subdir/file.txt", True),
        ("dir/**/file.txt", "dir/subdir1/subdir2/file.txt", True),
        (
            "dir/**/files/**/file.txt",
            "dir/subdir1/subdir2/files/file.txt",
            True,
        ),
        # Combinations
        ("**/*.txt", "file.txt", True),
        ("**/*.txt", "dir/file.txt", True),
        ("dir/**/*.txt", "dir/file.txt", True),
        ("dir/**/*.txt", "dir/subdir/file.txt", True),
        ("dir/**/*file*.txt", "dir/subdir/myfile1.txt", True),
        # Non-matches
        ("file.txt", "file.csv", False),
        ("dir/file.txt", "dir2/file.txt", False),
        (
            "*.txt",
            "dir/file.txt",
            False,
        ),  # * doesn't match directory separators
        ("dir/*.txt", "dir/subdir/file.txt", False),
        ("dir/red/**/src*.txt", "dir/red/red/srcfile.txt", True),
        ("dir/red/**/src/demo.txt", "dir/red/red/src/no/file.txt", False),
        # Test case for multiple potential matches with **
        (
            "**/nextsection/file.txt",
            "demo/nextsection/nextsection/file.txt",
            True,
        ),
        (
            "**/nextsection/other.txt",
            "demo/nextsection/nextsection/other.txt",
            True,
        ),
        (
            "**/nextsection/**/final.txt",
            "demo/nextsection/nextsection/final.txt",
            True,
        ),
        (
            "**/nextsection/**/final.txt",
            "demo/nextsection/something/nextsection/final.txt",
            True,
        ),
        # Test case to verify greedy vs non-greedy behavior
        (
            "demo/**/nextsection/final.txt",
            "demo/nextsection/nextsection/final.txt",
            True,
        ),
        (
            "demo/**/nextsection/final.txt",
            "demo/something/nextsection/final.txt",
            True,
        ),
        # Test case to verify first match is used
        (
            "**/nextsection/end.txt",
            "path/nextsection/nextsection/end.txt",
            True,
        ),
        (
            "**/nextsection/end.txt",
            "path/nextsection/other/nextsection/end.txt",
            True,
        ),
        # Test case for trailing slash, which is shorthand "path contains"
        (
            "**/dir_cursive/",
            "path/nextsection/dir_cursive/nextsection/end.txt",
            True,
        ),
    ]
    for pattern, target, expected in test_cases:
        assert glob_matcher(pattern, target) == expected, (
            f"Test failed for pattern {pattern} and target {target}"
        )
