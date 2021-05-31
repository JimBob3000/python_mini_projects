def fibonacci(max_int):
    # Setup initial variables
    n1, n2, n3 = 0, 1, 1

    while max_int >= n1:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3


# Show all numbers in the fibonacci sequence up to 30
fibonacci(30)
