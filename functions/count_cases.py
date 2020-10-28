# Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def upper_lower_count(s):
    a = 0 
    b = 0
    for x in s:
        if x.isupper():
           a += 1
        if x.islower():
           b += 1
    return [a, b]
s = input("Enter a word: ")
result = upper_lower_count(s)
print(result)
print("Upper case: ", result[0])
print("Lower case: ", result[-1])