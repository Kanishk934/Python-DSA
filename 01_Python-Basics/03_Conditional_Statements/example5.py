num = int(input("Enter a three-digit number: "))

a = num // 100
b = (num // 10) % 10
c = num % 10

sum_of_cubes = a ** 3 + b ** 3 + c ** 3

if sum_of_cubes == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")