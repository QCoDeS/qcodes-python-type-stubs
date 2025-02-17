"""
This type stub file was generated by pyright.
"""

import sys
from collections import UserList

"""Helper classs, functions and decorators"""
if sys.version_info >= (3, ):
    ...
else:
    ...
class HIDError(Exception):
    "Main HID error exception class type"
    ...


def simple_decorator(decorator): # -> (funct_target: Unknown) -> Unknown:
    """This decorator can be used to turn simple functions
    into well-behaved decorators, so long as the decorators
    are fairly simple. If a decorator expects a function and
    returns a function (no descriptors), and if it doesn't
    modify function attributes or docstring, then it is
    eligible to use this. Simply apply @simple_decorator to
    your decorator and it will automatically preserve the
    docstring and function attributes of functions to which
    it is applied."""
    ...

@simple_decorator
def logging_decorator(func): # -> (*args: Unknown, **kwargs: Unknown) -> Unknown:
    """Allow logging function calls"""
    ...

def synchronized(lock): # -> (function_target: Unknown) -> ((*args: Unknown, **kw: Unknown) -> Unknown):
    """ Synchronization decorator.
    Allos to set a mutex on any function
    """
    ...

class ReadOnlyList(UserList):
    "Read only sequence wrapper"
    def __init__(self, any_list) -> None:
        ...
    
    def __setitem__(self, index, value):
        ...
    


