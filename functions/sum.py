# Python function to sum all the numbers in a list.
def sum(list1):
    a = 0
    for x in list1:
      a += x
    return a
print(sum((2, 4, 6, 7, 8, 9)))