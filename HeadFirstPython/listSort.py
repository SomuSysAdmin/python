data = [6, 3, 1, 2, 4, 5]

"""
Python has a BIF for copied sorting, i.e., copying the original list and then sorting that list, which is then handed 
over to another object (to store the reference). In contrast, the list object itself has a `.sort()` function which 
doesn't create a new copy of the data, but replaces the original list with the sorted list (i.e., assigns the sorted 
list's reference to the original object, thus removing the original list). 
"""

print("\nCopying and Sorting: ")
sortedData = sorted(data)       # Copies and sorts
print("Original Array = " + str(data))
print("Sorted   Array = " + str(sortedData))

print("\nPerforming in-place Sort: ")
data.sort()     # In place sorting.
print("Original Array = " + str(data))

"""
To sort using .sort or sorted() in descending order, all we need to do is pass the argument reverse=True
"""
print("\nList in descending order:")
print(sorted(data, reverse = True))