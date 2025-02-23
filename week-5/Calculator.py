def Calculator(n):
    digit_1 = min(n, 9)
    digit_2 = max(0, min(n, 99) - 9)
    digit_3 = max(0, n - 99)

    