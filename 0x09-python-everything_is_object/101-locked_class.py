#!/usr/bin/python3
"""
This is a module that containts a class that avoids
dynmically created attributes
"""

class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
