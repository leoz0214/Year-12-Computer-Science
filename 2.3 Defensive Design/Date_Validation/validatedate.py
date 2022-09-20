"""
Write a program that asks the user to enter a date in the format DD/MM/YYYY. The program should validate the data in the following ways. The program should output that the date is valid or, if it isn’t, an error displaying which check failed:
There is some input.
The date is 10 characters long.
The date is in the correct format.
The day, month and year are all numbers.
The day and month are not less than 01.
The month is not more than 12.
The year is not less than 1900.
The day is not more than 29 if the month is 02.
The day is not more than 30 for months 02, 04, 06, 09 or 11.
The day is not more than 31 for months 01, 03, 05, 07, 08, 10 or 12.
The day can be 29 for month 02 if the year is exactly divisible by 4.
"""


# Dictionary storing days in each month.
DAYS_IN_EACH_MONTH = {
    1: 31,
    2: lambda year: 28 + is_leap_year(year), # Can be a leap year, add 1 if True. for 29.
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def is_leap_year(year: int) -> bool:
    """
    Checks if a year is a leap year.
    A leap year is divisble by 4 and if it is divisible by 100,
    it must also be divisible by 400.
    """
    return year % 4  == 0 and (year % 100 != 0 or year % 400 == 0)


def validate_date(date: str) -> bool:
    """
    Ensures that the date is valid based on a set of given criteria.
    The date must be in the format DD/MM/YYYY.
    """
    # Format check
    try:
        day, month, year = date.split("/")
        # Length check: 2 + 2 + 4 = 10
        if len(day) != 2 or len(month) != 2 or len(year) != 4:
            return False
    except ValueError:
        # More or less than 2 forward slashes.
        return False

    # Numeric check
    if any(not part.isdigit() for part in (day, month, year)):
        return False

    # Cast to integers
    day, month, year = map(int, (day, month, year))

    # Range checks
    if year < 1900:
        return False
    elif month == 2:
        return 1 <= day <= DAYS_IN_EACH_MONTH[2](year)
    return 1 <= day <= DAYS_IN_EACH_MONTH.get(month, -1)



    
