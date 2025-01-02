from html_compose.util_funcs import flatten_iterable


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
