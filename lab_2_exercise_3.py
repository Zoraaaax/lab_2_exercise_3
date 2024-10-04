def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("x" * n)
        else:
            print("x" + " " * (n - 2) + "x")


try:
    length = int(input("Enter the length of the square: "))
    if length < 2:
