def show():
    value=input("enter the value to check palindrome:").lower()
    reverse = value[::-1]

    if value == reverse:
        print(value, "is a palindrome")

    else:
        print(value,"is not a palindrome")

show()
