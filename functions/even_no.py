# Python program to print the even numbers from a given list.
def even(list1):
    a = []
    for x in list1:
      if x % 2 == 0:
          a.append(x)
    return a

result = even([2, 3, 4])
print(result)