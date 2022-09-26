"""
This module holds a factorial function with validation of input included.
"""


def factorial(n: int) -> int:
    """
    Calculates the factorial of a number.
    Factorial is only defined for non-negative integers.
    """
    validate(n)
    
    total = 1
    for i in range(1, int(n) + 1):
        total *= i
        
    return total


def validate(n: int) -> None:
    """
    Ensures factorial input data is valid
    """
    if isinstance(n, int):
        if n < 0:
            raise ValueError("Factorial is undefined for negative numbers")
    elif isinstance(n, float):
        if n.is_integer():
            if n < 0:
                raise ValueError("Factorial is undefined for negative numbers")
        else:
            raise ValueError("Factorial is undefined for non-integral numbers")
    else:
        raise TypeError(f"Expected integer, not {type(n).__name__}")
