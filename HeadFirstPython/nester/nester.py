# Modules are used to organize code for optimal sharing.
# Distribution utilities are used to actually share the module.

# A module is simply a file containing python code. The following is a module form of the nesting function:

"""
This python module provides a function called print_lol that is capable of printing each item in the list without
presenting any element in bracket format. Each list item is printed individually!
"""


def print_lol(the_list):

    """
    This function checks if the present item in the list is a list iteself. This detects sub-lists. Any number of items
    in sublists (subject to Python's limitations) can be printed by this function due to recursion.

    :param the_list:    The list which can contain multiple sub-lists nested at any level.
    :return:            none.
    """
    for item in the_list:
        if isinstance(item, list):
            print_lol(item)
        else:
            print(item)
