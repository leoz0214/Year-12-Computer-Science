import validatedate


def main() -> None:
    while True:
        date = input("Enter a date (DD/MM/YYYY) from 1900 and later: ")
        if validatedate.validate_date(date):
            print("Valid!")
        else:
            print("Invalid...")


if __name__ == "__main__":
    main()
