"""
Just like sets  in mathematics, the set data-structure ignores all duplicates and stores data in an unordered format.
The `set()` function is also called a factory function. Factory functions is used to create data items (structures) of a
particular type.
"""

# To create an empty set
distance = set()
print(distance)

# To create and initialize a set in one step:
distance = {10.6, 11, 8, 10.6, "two", 7}    # Duplicates are automatically ignored.
print(distance)

# To convert an existing list into a set:
distance_list = [10.6, 11, 8, 10.6, "two", 7]
print("\nList: " + str(distance_list))
distance = set(distance_list)
print("Set : " + str(distance))