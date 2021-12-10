def match(c):
    """
    return the matching char
        [(<{  ->  ])>}
    """
    chrs = "[{(<>)}]"
    return dict(zip(chrs, reversed(chrs))).get(c)


for a, b in ["<>", "[]", "{}", "()"]:
    assert match(a) == b and match(b) == a
