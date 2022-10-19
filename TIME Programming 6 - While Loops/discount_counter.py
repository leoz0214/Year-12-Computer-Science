import secrets


def discount_counter(start: int, stop: int) -> None:
    """
    Increases a discount randomly up to a point, displaying each step.
    """
    print(f"{start}% off")
    current = start
    while current < stop:
        current += secrets.choice(range(1, stop - current + 1))
        print(f"{current}% off")


def test():
    discount_counter(10, 60)
    discount_counter(1, 99)


test()
