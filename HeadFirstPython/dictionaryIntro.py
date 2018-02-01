"""
A dictionary is a special data structure that allows us to store data like a list, but with string indices like an 
associative array! So, the data values are associated with _keys_. Note that the keys must *not necessarily be strings*.

A dictionary is the preferred data structure whenever data has structure associated with it - especially in cases of 
hierarchy and not just order like in the cases of lists! 

It is extremely similar to _mappings_, _hashes_ or even _associative arrays_!
"""

# Basics: There are two ways of creating an empty dictionary:
cleese = {}
palin = dict()
print("Type of cleese : " + str(type(cleese)))
print("Type of palin  : " + str(type(palin)))

# Creating Dictionary with Data:
cleese['Name'] = 'John Cleese'  # Either specify the individual indices.
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
palin = {'Name': 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}     # Or the entire dict at once

# Accessing elements:
print("\n"+ palin['Name'], sep="")
print(cleese['Occupations'][-1])    # Accessing the inner list's last element of Occupations key for the dictionary.

# Adding data post-creation:
palin['Birthplace'] = "Broomhill, Sheffield, England"
cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England"
print("\n" + palin['Birthplace'], sep="")

"""
Unlike lists, however, the dictionaries don't maintain insertion order. Thus, the only ordering is via the associations. 
"""
print(palin)

