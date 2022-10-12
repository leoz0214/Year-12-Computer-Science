def generate_passcode(word: str) -> str:
    """
    Generates a passcode from a word,
    with its vowel indexes being the digits.
    """
    return "".join(
        str(i) for i, letter in enumerate(word.lower()) if letter in "aeiou")


def test():
    for word in ((
        "COMPUTER", "Python", "Abracadabra", "PASSWORD", "watrbllpwrd"
    )):
        print(word, generate_passcode(word))


test()