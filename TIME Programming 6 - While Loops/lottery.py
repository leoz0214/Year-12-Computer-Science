import secrets


def weeks_to_win_lottery(numbers: tuple) -> int:
    """
    Returns the number of weeks it took to win
    the lottery of 1 - 30 (order matters)
    """
    count = 1
    while tuple(secrets.choice(range(1, 31)) for _ in range(3)) != numbers:
        count += 1
    return count


def test():
    print(weeks_to_win_lottery((6, 14, 23)))


test()
