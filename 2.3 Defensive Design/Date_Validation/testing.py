import unittest

from validatedate import validate_date as validate


VALID_DATES = (
    "14/02/2007",
    "01/01/1900",
    "29/02/2020",
    "31/10/7234",
    "29/02/2400",
    "27/12/1999",
    "25/12/1947",
    "21/04/2021",
    "12/09/2022",
    "02/02/1900",
    "28/02/1949",
    "28/02/1952",
    "05/11/2000",
    "31/12/1999"
)


INVALID_DATES = {
    "1/1/1",
    "Hello world",
    "//",
    "///////////////////////",
    "2007/14/02",
    "25345-345--w-r=e=-=-3=-pv=-",
    "14-02-2007",
    "1/1/1999",
    "31/12/1899",
    "29/02/1900",
    "",
    " ",
    "31/09/1940",
    "3/10/1403",
    "30/02/2020",
}


class TestDateValidator(unittest.TestCase):

    def test_valid_dates(self) -> None:
        for date in VALID_DATES:
            self.assertTrue(validate(date))

    def test_invalid_dates(self) -> None:
        for date in INVALID_DATES:
            self.assertFalse(validate(date))


if __name__ == "__main__":
    unittest.main()
