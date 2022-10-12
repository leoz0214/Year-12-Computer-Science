def ascii_art(string: str) -> None:
    """
    Displays ASCII art in the specified format.
    """
    string = string.upper()
    operators = "+-" * len(string) + "+"
    print(operators)
    print("\n|" + "|".join(string) + "|\n")
    print(operators)


def test():
    ascii_art("Leo Zhang")
    ascii_art("Mr C")
    ascii_art("!")


test()
