def fibonacci(n):
    """
    Calculate the nth term of a fibonacci sequence

    Arg:
        n (int): nth term of the fibonacci sequence to calculate

    Returns:
        int: nth term of the fibonacci sequence,
             equal to the sum of the previous two terms

    Examples:
        >>> fibonacci(1)
        1
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)