def collatz(number):
    while number !=1:
        print(number)
        if number % 2 == 0:         #If the number is even
            number = int(number // 2)
        else:                 #If the number is odd
            number = int(3 * number + 1)
    else:
        print(number)

def main():
    try:
        number = int(input("Enter Number: "))
        collatz(number)
    except ValueError:
        print("Invalid Input")
if __name__ == "__main__":
    main()
