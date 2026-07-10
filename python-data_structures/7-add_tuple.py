#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples based on their first 2 elements."""
    # Ensure both tuples have at least 2 elements by appending zeros
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Sum only the first two elements
    return (a[0] + b[0], a[1] + b[1])
