def is_neon_number(num):
    square = num ** 2
    digits_sum = sum(int(digit) for digit in str(square))
    return digits_sum == num
num = int(input("Enter a number: "))
if is_neon_number(num):
    print(num, "is a neon number.")
else:
    print(num, "is not a neon number.")