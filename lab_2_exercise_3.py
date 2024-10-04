def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("x" * n)
        else:
