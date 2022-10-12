def fizz_buzz(last: int) -> None:
    """
    Outputs numbers from 1 to n (inclusive).
    Multiples of 3 get replaced with Fizz.
    Multiples of 5 get replaced with Buzz.
    Multiples of 15 get replaced with FizBuzz.
    Bottom has priority.
    """
    for number in range(1, last + 1):
        if number % 15 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


def test():
    fizz_buzz(30)


test()
