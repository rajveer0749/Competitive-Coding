number = input("Enter a number: ")

values = list(number)

if values == values[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")