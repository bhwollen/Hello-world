number = int(input('Input a number 0 - 1000: '))
first_digit = number % 10
number = number // 10
second_digit = number % 10
number = number // 10
third_digit = number % 10
print(first_digit + second_digit + third_digit)
