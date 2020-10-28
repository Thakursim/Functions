# Python function that takes a number as a parameter and check the number is prime or not.
def prime_or_not(a):
    if a % 2 == 0:
        print("Yes, it is a prime number")
    else:
        print("No, it is not a prime number")
    return (a)
a = int(input("Enter a number: "))
print(prime_or_not(a))