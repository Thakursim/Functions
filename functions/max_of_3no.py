# Python function to find the Max of three numbers.
def max(a, b, c):
    if a>b and a>c:
        print("Max=", a)
    elif b>c and b>a:
        print("Max=", b)
    elif c>a and c>b:
        print("Max=", c)
max(6,7,9)