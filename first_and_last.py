def is_first_and_last_equal(numbers):
    first = numbers[0]
    last = numbers[-1]

    if first == last:
        return True
    return False


numbers = [4, 6, 2, 1, 4]
print(f"Is first and last equal: {is_first_and_last_equal(numbers)}")
