# Recursive stack:

# print numbers in reverse order from that entered. eg, if input is 1, print must be 5 4 3 2 1


def reverse_num(a, n):
    # base case:
    if a == n:
        return

    reverse_num(a + 1, n)
    print(
        a, end=" "
    )  # bfore a printed, fn is called again, to the input goes to recursive stack


reverse_num(1, 6)
