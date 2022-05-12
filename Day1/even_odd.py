def evenOdd():
    number = int(input("Enter An Integer Number: "))
    if(number%2 == 0):
        print(number,"Number is even")
    else:
        print(number,"Number is odd")
    return number

if __name__ == "__main__":
    evenOdd()