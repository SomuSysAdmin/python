# Modules are used to organize code for optimal sharing.
# Distribution utilities are used to actually share the module.

# A module is simply a file containing python code. The following is a module form of the nesting function:

"""
This python module provides a function called print_lol that is capable of printing each item in the list without
presenting any element in bracket format. Each list item is printed individually!
"""


def print_lol(the_list, level=0):

    """
    This function checks if the present item in the list is a list iteself. This detects sub-lists. Any number of items
    in sublists (subject to Python's limitations) can be printed by this function due to recursion. An argument of level
    is also required to declare how many tabstops should be added before each sublist. This behavior can be stopped with
    an initial level of 0.

    :param the_list:    The list which can contain multiple sub-lists nested at any level.
    :param level:      The number of indentations for each sub-list. This is an optional argument with the default val=0
    :return:            none.
    """
    for item in the_list:
        if isinstance(item, list):
            if level != 0:
                print_lol(item, level+1)
            else:
                print(item, 0)
        else:
            if level != 0:
                for num in range(level-1):        # The range BIF takes an integer(n) and generates a sequence from 0...(n-1).
                    print("\t", end="")
            print(item)
