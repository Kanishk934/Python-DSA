def reverse_number(num):

    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10

    return reverse


print(reverse_number(12345))