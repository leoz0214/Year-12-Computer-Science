def dispense_minimum_notes(withdrawal: int) -> None:
    """
    Displays the notes dispensed by the ATM (minimum).
    """
    print(f"Withdraw: £{withdrawal}")
    for value in (20, 10, 5):
        while withdrawal >= value:
            print(f"Dispense: £{value}")
            withdrawal -= value


def test():
    for w in (115, 10, 20, 5, 50, 255):
        dispense_minimum_notes(w)


test()
