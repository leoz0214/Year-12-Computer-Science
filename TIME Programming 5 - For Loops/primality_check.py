def is_prime(number: int) -> bool:
    """
    Checks if a number is prime.
    A prime number only has divisors
    of 1 and itself.
    """
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    
    for n in range(3, int(number ** 0.5) + 1, 2):
        if number % n == 0:
            return False
    
    return True


def test():
    for number in (-2, -1, 0, 1, 2, 3, 4, 5, 7, 97, 2147231, 3148812, 81281):
        print(number, is_prime(number))
    # Not designed to generate, but proves functionality nonetheless.
    for power in range(1, 8):
        maximum = 10 ** power
        print(
            f"Number of primes between 1 and {maximum}:",
            len([n for n in range(1, maximum + 1) if is_prime(n)]))


test()