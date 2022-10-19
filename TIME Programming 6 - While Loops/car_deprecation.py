def car_deprecation(
    year: int, value: float, minimum_resale_value: float) -> None:
    """
    Displays the deprecation of a car -
    30% in the first and second years and 20% each year after.
    """
    print("{}: £{:.2f}".format(year, value))
    for _ in range(2):
        if value * 0.7 < minimum_resale_value:
            return
        year += 1
        value *= 0.7
        print("{}: £{:.2f}".format(year, value))

    while value * 0.8 > minimum_resale_value:
        year += 1
        value *= 0.8
        print("{}: £{:.2f}".format(year, value))


def test():
    car_deprecation(2020, 12500, 6000)
    car_deprecation(42385, 31415.90, 1000)
    car_deprecation(1000, 1, 0.9)


test()
        
        
