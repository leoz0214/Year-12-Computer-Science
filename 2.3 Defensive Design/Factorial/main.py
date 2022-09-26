from factorial import factorial


if __name__ == "__main__":
    while True:
        number = input(
            "Enter a non-negative integer to calculate its factorial: ")
        try:
            number = int(number) if number.isdigit() else float(number)
            if number > 1000:
                print("Too big...\n")
                continue
        except ValueError:
            pass
        
        try:
            print(f"{int(number)}! = {factorial(number)}")
        except Exception as e:
            print(e)
        print()
