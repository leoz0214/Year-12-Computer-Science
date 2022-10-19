def compound_interest(
    current_balance: float, interest_rate: float, desired_balance: float
) -> None:
    """
    Adds compound interest and displays balance after each year
    until desired balance is reached.
    """
    year = 1
    while current_balance < desired_balance:
        current_balance *= (1 + interest_rate)
        print("Year {}: £{:.2f}".format(year, current_balance))
        year += 1


def test():
    compound_interest(100, 0.04, 200)
    compound_interest(7.77, 1, 1718.84)


test()
