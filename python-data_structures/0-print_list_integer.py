#!/usr/bin/python3
"""
This module provides a function to print all integers of a list.
Each integer is printed on a new line using str.format().
"""


def print_list_integer(my_list=[]):
    """
    Prints all integers of a list, one per line.

    Args:
        my_list (list): A list of integers. Defaults to an empty list.
    """
    for i in my_list:
        print("{:d}".format(i))
