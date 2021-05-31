def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return"Fizz"
    return number


# From 1 to 15
for number in range(1, 16):
    print(fizz_buzz(number))
