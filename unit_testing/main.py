def add_five(num: int | str) -> int:
    if type(num) not in [int, str]:
        return TypeError("Please enter a number")

    try:
        return int(num) + 5
    except ValueError as err:
        return err


# Notice the difference between returning and raising errors in tests
