#!/usr/bin/python3
""" Module that returns true if object is exactly an instance of specified class
"""


def is_same_class(obj, a_class):
    """ Function that returns True/False if obj is a type of a_class
    Args:
        obj: object
        a_class: class type
    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return type(obj) is a_class
