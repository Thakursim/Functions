#  Python function to check whether a number is in a given range.
def check(a, b, c):
    if a < b < c:
        return True
    else:
        return False

a = int(input("Enter a range(min): "))
c = int(input("Enter a range(max): "))
b = int(input("Enter a number: "))

print(check(a, b, c))