# Python function that takes a list and returns a new list with unique elements of the first list.

def list_to_newlist(list1):
    a = set(list1)
    b = list(a)
    return b
list1 = [2, 4, 5, 6, 2]
print(list_to_newlist(list1))