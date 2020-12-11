from day07 import parse, can_hold


def test_parse():
    assert parse(
        "muted lime bags contain 4 drab lavender bags, 1 clear orange bag, 2 striped black bags.\n"
    ) == (
        "muted lime",
        [
            (4, "drab lavender"),
            (1, "clear orange"),
            (2, "striped black"),
        ],
    )

    assert parse(
        "light salmon bags contain 5 dotted olive bags, 4 wavy lavender bags.\n"
    ) == (
        "light salmon",
        [
            (5, "dotted olive"),
            (4, "wavy lavender"),
        ],
    )

    assert parse("bright violet bags contain 1 bright purple bag.\n") == (
        "bright violet",
        [(1, "bright purple")],
    )

    assert parse("plaid fuchsia bags contain no other bags.\n") == (
        "plaid fuchsia",
        []
    )


def test_can_hold():
    container = {"dim chartreuse": 2, "shiny gold": 3}
    assert can_hold(container, "shiny gold", 1) == 1
    assert can_hold(container, "shiny gold", 2) == 1
    assert can_hold(container, "shiny gold", 3) == 1
    assert can_hold(container, "shiny gold", 4) == 0
    assert can_hold(container, "orange", 1) == 0
