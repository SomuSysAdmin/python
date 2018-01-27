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

