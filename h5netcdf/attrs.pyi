"""
This type stub file was generated by pyright.
"""

from collections.abc import MutableMapping

_HIDDEN_ATTRS = ...
class Attributes(MutableMapping):
    def __init__(self, h5attrs, check_dtype, h5py_pckg) -> None:
        ...
    
    def __getitem__(self, key): # -> NDArray[Any] | str | int | generic | bool | float | complex | bytes | memoryview | list[Unknown]:
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __delitem__(self, key): # -> None:
        ...
    
    def __iter__(self): # -> Generator[Unknown, None, None]:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __repr__(self): # -> str:
        ...
    


