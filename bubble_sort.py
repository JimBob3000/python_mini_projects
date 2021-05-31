def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(0, len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                # Swap current number with next number in sequence
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]


numbers = [2, 5, 3, 9, 11, 4]
print(f"Starting number list: {numbers}")
bubble_sort(numbers)
print(f"Ending number list: {numbers}")
