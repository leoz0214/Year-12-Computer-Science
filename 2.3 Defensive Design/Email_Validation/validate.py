"""
Write a program that validates an email address: 
It must contain an @ symbol.
Capital letters must be converted to lower case.
A dot cannot be the first or last character.  
Double dots are not permitted.
"""


def validate(email: str) -> None:
    """
    A procedure which validates an email based on the given criteria.
    """
    # Type check
    if not isinstance(email, str):
        print("Email must be a string")
        return

    valid = True
    # Presence check
    if "@" not in email:
        valid = False
        print("Email must contain '@'")
    # Format check
    if not email.islower():
        valid = False
        print("Email must be lowercase")
    # Format check
    if email.startswith("."):
        valid = False
        print("Email cannot start with a dot ('.')")
    # Format check
    if email.endswith("."):
        valid = False
        print("Email cannot end with a dot ('.')")
    # Format check
    if ".." in email:
        valid = False
        print("Double dots are not permitted")

    if valid:
        print("Email is valid!")

    
