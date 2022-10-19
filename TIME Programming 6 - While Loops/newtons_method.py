def SqRoot(number: float) -> float:
    """
    Calculates the square root of a number using Newton's method
    """
    if number == 0:
        return 0
    root = number
    previous = None
    while root != previous:
        previous = root
        root = 0.5 * (root + number / root)
    return root


def test():
    for i in range(100_000):
        assert round(SqRoot(i), 8) == round(i ** .5, 8)
    print("Works!")


test()
