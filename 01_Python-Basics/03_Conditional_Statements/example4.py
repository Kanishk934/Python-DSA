month = int(input("Enter month number: "))
year = int(input("Enter year: "))

if month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
elif 1 <= month <= 12:
    print("31 days")
else:
    print("Invalid month")