fav_movies = ["The Holy Grail", "The Life of Brian"]

print("Printed using for-each loop:")
for each_flick in fav_movies:   # Basic For-Each loop --> each_flick is called the "target identifier"
    print(each_flick)           # This part of the loop is called the "suite"

print("\nPrinted using while loop:")
count=0
while(count<len(fav_movies)):
    print(fav_movies[count])    # State information such as the present index has to be considered here!
    count+=1                    # IndexError will be caused if count is not a valid index for the list.
# Note that python is case sensitive and thus var and Var are different variables. A "NameError" is thrown otherwise.

# Nested Lists:

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
            ["Graham Chapman",
                ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
print("\nActor: ", movies[4][1][3])

print("\n", movies)
for each_flick in movies:
    print(each_flick)       # This prints the inner list as-is. To print it properly, we need a way to check if the
                            # data is a list.

print("\n\nPrinted after checking with 'isinstance' to see whether element is a sub-list: ")
for each_flick in movies:
    if isinstance(each_flick, list):        # This method checks if the variable is a certain type of object - like list
        print("Main Actors: ", end="")      # A way to eliminate the newline printed at the end of every print statement
        for each_actor in each_flick:
            if isinstance(each_actor, list):
                print("Supporting Actors: ", end="")
                for each_supAct in each_actor:
                    print(each_supAct)
            else:                           # Note that even the else statement requires the use of a colon
                print(each_actor)
    else:
        print(each_flick)

# We can see a list of all the BIFs in Python with the use of: dir(__builtins__) in the python shell.
# To find help about a certain function (say 'input()') we can merely type 'help(input)' at the console.

# Functions in Python:


def print_lol(the_list):                    # The def keyword is used to define a new function.
    for list_item in the_list:
        if isinstance(list_item, list):
            print_lol(list_item)
        else:
            print(list_item)


print("\n\nPrinted with a recursive function: ")
print_lol(movies)   # Note that there should be two blank lines before/after a function or class definition.
# This is a coding standard and not an actual error.
