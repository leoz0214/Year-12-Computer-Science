from math import factorial
from decimal import Decimal
from collections import Counter


def get_sequence(numbers: list[int]) -> list[tuple[float, int]]:
    """
    Finds nth term for sequence values.
    """
    parts = []
    for exponent in range(len(numbers) - 1, -1, -1):
        nums = [numbers]
        new = []

        while True:
            for i in range(1, len(nums[-1])):
                new.append(Decimal(nums[-1][i]) - Decimal(nums[-1][i - 1]))
            if not new:
                break
            nums.append(new)
            new = []

        count = Decimal(nums[-1][0])
        coef = Decimal(count / factorial(exponent))
        numbers.pop()
        if coef:
            parts.append((coef, exponent))
            numbers = [
                Decimal(n - coef * i ** exponent)
                for i, n in enumerate(numbers, 1)]
    return parts


SEQUENCE = get_sequence(
    [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
        1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10])


def get_letter_value(letter: str) -> int:
    """
    Returns letter value.
    """
    n = ord(letter.lower()) - ord("a") + 1
    total = Decimal(0)
    for coef, exponent in SEQUENCE:
        total += Decimal(coef * n ** exponent)
    return int(round(total))


def get_word_value(word: str) -> int:
    """
    Returns total word value.
    """
    counts = Counter(word.lower())
    return sum(
        get_letter_value(letter) * count for letter, count in counts.items())


def test():
    for word in (
        "HELLO", "Python", "programming",
        "QUEST", "SUPERCALIFRAGILISTICEXPIALIDOCIOUS"
    ):
        print(word, get_word_value(word))


test()