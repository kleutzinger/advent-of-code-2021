def match(c):
    """
    return the matching char
        [(<{  ->  ])>}
    """
    for pair in [set(s) for s in ["()", "[]", "{}", "<>"]]:
        if c in pair:
            return (pair - set([c])).pop()


for a, b in ["<>", "[]", "{}", "()"]:
    assert match(a) == b and match(b) == a
