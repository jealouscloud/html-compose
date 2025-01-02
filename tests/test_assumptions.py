"""

These are assumptions that are used elsewhere in the repo
They usually have no bearing on the code functionality itself

"""


def test_args():
    """
    This is the logic that base_element.append uses for args
    """
    input_data = (1, 2, 3, 4, 5)

    def demo(*args):
        # If you pass a tuple manually, it needs to be unboxed
        if (
            isinstance(args, tuple)
            and len(args) == 1
            and isinstance(args[0], tuple)
        ):
            return args[0]
        return args

    # demo(1,2,3)
    assert demo(*input_data) == input_data
    assert demo(1, 2, 3, 4, 5) == input_data
    assert demo(input_data) == input_data


def test_join_perf():
    """
    We use an LRU cache to speed up the join_attr function

    This test confirms the hypothesis that the cache is faster than no cache
    As long as there are attrs that are frequently used

    This is implemented in ElementBase

    """
    import random
    import string
    from functools import lru_cache
    from time import perf_counter

    random.seed(0)
    ATTRS_PER_ELEMENT = 10000
    TOP_ATTR_COUNT = 100
    ATTR_MAX_SIZE = 100
    ELEMENT_COUNT = 10

    def generate_random_string(length: int) -> str:
        return "".join(
            random.choices(string.ascii_letters + string.digits, k=length)
        )

    def generate_attrs(count, max_size):
        keys = [generate_random_string(10) for _ in range(count)]
        values = [
            generate_random_string(random.randint(1, max_size))
            for _ in range(count)
        ]
        attr_dict = {}
        for i in range(count):
            attr_dict[keys[i]] = values[i]
        return attr_dict

    # Generate a bunch of pseudo elements
    pseudo_elements = [
        generate_attrs(ATTRS_PER_ELEMENT, ATTR_MAX_SIZE)
        for _ in range(ELEMENT_COUNT)
    ]

    def join_attr(key, value):
        return f'{key}="{value}"'

    start = perf_counter()
    for element in pseudo_elements:
        _ = " ".join((join_attr(k, v) for k, v in element.items()))

    end = perf_counter()
    no_cache = end - start
    print(f"\nTime taken without cache: {end-start}")
    top_attrs = generate_attrs(TOP_ATTR_COUNT, ATTR_MAX_SIZE)
    infrequent_attrs = generate_attrs(10000, 100)  # Big spread
    infr_keys = list(infrequent_attrs.keys())

    pseudo_elements = []
    attr_delta = ATTRS_PER_ELEMENT - TOP_ATTR_COUNT

    for _ in range(ELEMENT_COUNT):
        el = top_attrs.copy()
        infreq_selected = []
        for k in [
            random.choice(infr_keys)
            for _ in range(ATTRS_PER_ELEMENT - TOP_ATTR_COUNT)
        ]:
            infreq_selected.append((k, infrequent_attrs[k]))

        ratio = attr_delta / TOP_ATTR_COUNT
        infreq_i = 0
        for k, v in top_attrs.items():
            el[k] = v
            # Add infrequent attrs
            for _ in range(int(ratio)):
                ifq = infreq_selected[infreq_i]
                el[ifq[0]] = ifq[1]
        pseudo_elements.append(el)

    join_attr = lru_cache(maxsize=TOP_ATTR_COUNT)(join_attr)

    start = perf_counter()
    for element in pseudo_elements:
        _ = " ".join((join_attr(k, v) for k, v in element.items()))

    end = perf_counter()
    print(f"Time taken with cache: {end-start}")

    with_cache = end - start

    assert with_cache < no_cache, "Cache should be faster than no cache"


def test_yield_from():
    arr = [1, 2, 3, 4, 5]

    def gen():
        yield from arr

    assert list(gen()) == arr

    gen_2 = (x for x in arr)
    assert list(gen_2) == arr
