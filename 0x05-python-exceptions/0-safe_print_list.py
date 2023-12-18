#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print x elements of list.

    Args:
     my_list (list): the list to print element from.
     x(int): the number of elements in lists.

    Returns:
    the elements printed.
    """
    for i in range(0,x):
        try:
            print("{}".format(my_list[i],end="")
            i++
        except IndexError:
           break
        print("")
        return(i)
