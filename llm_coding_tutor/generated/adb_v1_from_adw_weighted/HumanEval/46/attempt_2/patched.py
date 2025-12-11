def fib4\(n: int\):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4\(0\) -> 0
    fib4\(1\) -> 0
    fib4\(2\) -> 2
    fib4\(3\) -> 0
    fib4\(n\) -> fib4\(n-1\) \+ fib4\(n-2\) \+ fib4\(n-3\) \+ fib4\(n-4\)\.
    Please write a function to efficiently compute the n-th element of the fib4 number sequence\.  Do not use recursion\.
    >>> fib4\(5\)
    4
    >>> fib4\(6\)
    8
    >>> fib4\(7\)
    14
    """
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        # Initialize the first four numbers of the sequence
        fib4_0 = 0
        fib4_1 = 0
        fib4_2 = 2
        fib4_3 = 0
        # Compute the n-th element iteratively
        for i in range\(4, n \+ 1\):
            fib4_next = fib4_0 \+ fib4_1 \+ fib4_2 \+ fib4_3
            fib4_0