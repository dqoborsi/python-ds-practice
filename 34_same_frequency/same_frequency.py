def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    str_num1 = str(num1)
    str_num2 = str(num2)

    counts1 = []
    counts2 = []

    for dig1 in str_num1:
        counts1.append(str_num1.count(dig1))

    for dig2 in str_num2:
        counts2.append(str_num2.count(dig2))

    if counts1 == counts2:
        return True

    return False