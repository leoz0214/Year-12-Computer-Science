def is_happy(number: int) -> bool:
    """
    Returns True if a number is happy, else False.
    """
    while True:
        number = sum(digit ** 2 for digit in map(int, str(number)))
        if number == 1:
            return True
        elif number == 4:
            return False


def test():
    for i in range(1, 100):
        print(i, is_happy(i), end=" ")


test()