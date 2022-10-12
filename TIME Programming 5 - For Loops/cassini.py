def OddParity(binary_sequence: str) -> bool:
    """
    Returns True if number of ones in the sequence
    is odd, else False.
    """
    return bool(sum(map(int, binary_sequence)) % 2)


def test():
    for sequence in (
        "1", "0", "10", "11", "1100101",
        "1110101", "11111", "000", "1111"
    ):
        print(sequence, OddParity(sequence))


test()