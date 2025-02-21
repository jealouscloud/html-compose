"""

These are assumptions that are used elsewhere in the repo
They usually have no bearing on the code functionality itself

"""

from time import perf_counter


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
    print(f"\nTime taken without cache: {end - start}")
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
    print(f"Time taken with cache: {end - start}")

    with_cache = end - start

    assert with_cache < no_cache, "Cache should be faster than no cache"


def test_yield_from():
    arr = [1, 2, 3, 4, 5]

    def gen():
        yield from arr

    assert list(gen()) == arr

    gen_2 = (x for x in arr)
    assert list(gen_2) == arr


def test_disassembly():
    """
    Test work actually done in python for a big argument list
    """

    def demo(**kwargs):
        pass

    class DemoDict:
        """
        Theory: Dictionary is optimized and building one with a generator
        May be faster than stacking
        """

        def _process_attr(self, attr_name, attr_value):
            pass

        def __init__(
            self,
            id=None,
            class_=None,
            download=None,
            href=None,
            hreflang=None,
            ping=None,
            referrerpolicy=None,
            rel=None,
            target=None,
            type=None,
            attrs=None,
            children=None,
        ) -> None:
            demo(
                type="a",
                void_element=False,
                id=id,
                class_=class_,
                attrs=attrs,
                children=children,
            )
            attrs = {
                k: v
                for k, v in {
                    "download": download,
                    "href": href,
                    "hreflang": hreflang,
                    "ping": ping,
                    "referrerpolicy": referrerpolicy,
                    "rel": rel,
                    "target": target,
                    "type": type,
                }.items()
                if v is not None and v is not False
            }

    class Demo:
        def _process_attr(self, attr_name, attr_value):
            pass

        def __init__(
            self,
            id=None,
            class_=None,
            download=None,
            href=None,
            hreflang=None,
            ping=None,
            referrerpolicy=None,
            rel=None,
            target=None,
            type=None,
            attrs=None,
            children=None,
        ) -> None:
            demo(
                type="a",
                void_element=False,
                id=id,
                class_=class_,
                attrs=attrs,
                children=children,
            )
            if not (download is None or download is False):
                self._process_attr("download", download)
            if not (href is None or href is False):
                self._process_attr("href", href)
            if not (hreflang is None or hreflang is False):
                self._process_attr("hreflang", hreflang)
            if not (ping is None or ping is False):
                self._process_attr("ping", ping)
            if not (referrerpolicy is None or referrerpolicy is False):
                self._process_attr("referrerpolicy", referrerpolicy)
            if not (rel is None or rel is False):
                self._process_attr("rel", rel)
            if not (target is None or target is False):
                self._process_attr("target", target)
            if not (type is None or type is False):
                self._process_attr("type", type)

    # Uncomment to view disassembly
    # import dis

    # dis.dis(Demo.__init__)
    # dis.dis(DemoDict.__init__)
    # raise Exception("Disassemble and analyze disassembly output")

    d2start = perf_counter()
    for i in range(100000):
        DemoDict(href="https://example.com")
    d2end = perf_counter()

    dstart = perf_counter()
    for i in range(100000):
        Demo(href="https://example.com")
    dend = perf_counter()

    test1_delta = dend - dstart
    test2_delta = d2end - d2start
    print(f"Test 1: {test1_delta} seconds")
    print(f"Test 2: {test2_delta} seconds")
    # If this test passes, then a huge attr list of if (not x is or x is)
    # is faster. The library uses this assumption.
    assert test2_delta > test1_delta
