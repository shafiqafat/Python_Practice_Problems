year = int(input("Enter Year: "))

if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} isn't a Leap Year.")