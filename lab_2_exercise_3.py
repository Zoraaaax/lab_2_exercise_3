def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("x" * n)
        else:
            print("x" + " " * (n - 2) + "x")


try:
    length = int(input("Enter the length of the square: "))
    if length < 2:
        print("Invalid! Length must be 2 or greater.")
    else:
        hollow_square(length)

except ValueError:
    print("Invalid input! Please enter an integer.")
