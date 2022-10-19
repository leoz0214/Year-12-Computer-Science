from math import log2, floor


def denary_to_binary(denary: int) -> str:
    """
    Converts denary to binary.
    """
    if not denary:
        return "0"
    digits = floor(log2(denary)) + 1
    parts = []
    for n in range(digits - 1, -1, -1):
        if denary >= 2 ** n:
            parts.append("1")
            denary -= 2 ** n
        else:
            parts.append("0")
    return "".join(parts)


def test():
    for i in range(33):
        print(denary_to_binary(i))


test()
        
