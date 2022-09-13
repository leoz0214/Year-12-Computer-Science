from validate import validate


def main():
    while True:
        email = input("Enter an email: ")
        validate(email)
        print()


if __name__ == "__main__":
    main()
