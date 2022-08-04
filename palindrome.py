def show():
    value=input("enter the number to check palindrome:")

    reverse = value[::-1]

    if value == reverse:
        print("yes, it is palindrome")

    else:
        print("no, it is not palindrome")

show()
