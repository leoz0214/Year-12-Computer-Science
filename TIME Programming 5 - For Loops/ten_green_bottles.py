def ten_green_bottles() -> None:
    """
    Outputs the 10 green bottles children's song.
    """
    
    for bottles in range(10, 0, -1):
        plural_add = "s" if bottles != 1 else ""
        plural_add_next = "s" if bottles != 2 else ""
        print(
            f"{bottles} green bottle{plural_add} hanging on the wall,\n" * 2 +\
            "And if one green bottle should accidentally fall,\n" +\
            f"There'll be {bottles - 1} green bottle{plural_add_next} " +\
            "hanging on the wall.\n")


ten_green_bottles()
