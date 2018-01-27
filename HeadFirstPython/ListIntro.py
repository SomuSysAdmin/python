# This is a demo of the functionality of Lists.

movies = ["The Holy Grail",         # Index = 0
          "The Life of Brian",      # Index = 1
          "The Meaning of Life"]    # Index = 2

print("Movie at index 1: ", movies[1])

cast = ["Cleese", 'Palin', 'Jones', "Idle"]     # cast is actually a python collection object.
print(cast)         # Functions like print are called Build In Functions (BIFs)
print(len(cast))    # len is another such BIF that prints the length of an object.
print(cast[2])

# Adding and removing data:
cast.append("Gilliam")      # Add an element to the end of the list
print(cast)
cast.pop()      # To remove the last element in the list
print(cast)
cast.pop(1)     # To delete an element at a specific index
print(cast)

cast.insert(1, "Palin")     # To insert element at a specific index
print(cast)
cast.extend(["Gilliam", "Chapman"])
print(cast)
cast2=["Test1", "Test2", "Test3"]
cast.extend(cast2)      # Add an entire list to the end of the current list
print(cast)
cast.pop(-2)            # Remove the element with the 2nd last index
cast.pop(len(cast)-1)   # Removing the last element by calculating index
print(cast)
cast.remove("Test1")
print(cast)

# Ex-1
movies.insert(1,1975)
movies.insert(3,1979)
movies.append(1983)
print(movies)