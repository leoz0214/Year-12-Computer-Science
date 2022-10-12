def times_tables(n: int) -> None:
    """
    Displays the first 12 multiples of n as times tables.
    """
    print("\n".join(f"{i} x {n} = {i * n}" for i in range(1, 13)))


def test() -> None:
    for i in range(3):
        times_tables(i)


test()
