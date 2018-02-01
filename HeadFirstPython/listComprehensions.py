mins = [1, 2, 3]
secs = [m*60 for m in mins]
"""
list comprehensions always have the same format:
`new_list = [ function(x) for x in old_list ]` where _x_ is the target identifier and the *function(x)* is the 
transformation. 

This is somewhat of a _functional programming_ concept. 

NOTE that list comprehensions can only deal with situations where each item in the list has to be transformed, and thus
if the transformation has to occur on the basis of certain criteria, then it doesn't work. 
"""
print(secs)

# Transforming meters into feet:
meters = [1, 10, 3]
feet = [m*3.281 for m in meters]
print(feet)

# Lower and Mixed case to uppercase:
lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]      # .upper() method of a string converts it to all-uppercase.
print(upper)

# Converting string to float using float() BIF:
timeStr = ['2.12', '2.76', '2.35']
timeFloat = [float(t) for t in timeStr]
print(timeFloat)