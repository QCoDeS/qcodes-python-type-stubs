"""
This type stub file was generated by pyright.
"""

import sys

PY2 = ...
if PY2:
    string_types = ...
else:
    string_types = ...
def with_metaclass(meta, *bases):
    """Create a base class with a metaclass."""
    ...

class _ObjectProxyMethods:
    @property
    def __module__(self):
        ...
    
    @__module__.setter
    def __module__(self, value): # -> None:
        ...
    
    @property
    def __doc__(self):
        ...
    
    @__doc__.setter
    def __doc__(self, value): # -> None:
        ...
    
    @property
    def __dict__(self):
        ...
    
    @property
    def __weakref__(self):
        ...
    


class _ObjectProxyMetaType(type):
    def __new__(cls, name, bases, dictionary): # -> Self@_ObjectProxyMetaType:
        ...
    


class ObjectProxy(with_metaclass(_ObjectProxyMetaType)):
    __slots__ = ...
    def __init__(self, wrapped) -> None:
        ...
    
    @property
    def __name__(self): # -> Any:
        ...
    
    @__name__.setter
    def __name__(self, value): # -> None:
        ...
    
    @property
    def __class__(self): # -> Any:
        ...
    
    @__class__.setter
    def __class__(self, value): # -> None:
        ...
    
    def __dir__(self): # -> list[str]:
        ...
    
    def __str__(self) -> str:
        ...
    
    if notPY2:
        def __bytes__(self): # -> bytes:
            ...
        
    def __repr__(self): # -> str:
        ...
    
    def __reversed__(self): # -> reversed[Unknown | Any]:
        ...
    
    if notPY2:
        def __round__(self): # -> Any:
            ...
        
    if sys.hexversion >= 50790400:
        def __mro_entries__(self, bases): # -> tuple[Unknown | Any]:
            ...
        
    def __lt__(self, other) -> bool:
        ...
    
    def __le__(self, other) -> bool:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __gt__(self, other) -> bool:
        ...
    
    def __ge__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __nonzero__(self): # -> bool:
        ...
    
    def __bool__(self): # -> bool:
        ...
    
    def __setattr__(self, name, value): # -> None:
        ...
    
    def __getattr__(self, name): # -> Any:
        ...
    
    def __delattr__(self, name): # -> None:
        ...
    
    def __add__(self, other):
        ...
    
    def __sub__(self, other):
        ...
    
    def __mul__(self, other):
        ...
    
    def __div__(self, other):
        ...
    
    def __truediv__(self, other): # -> Any:
        ...
    
    def __floordiv__(self, other):
        ...
    
    def __mod__(self, other):
        ...
    
    def __divmod__(self, other): # -> Any:
        ...
    
    def __pow__(self, other, *args): # -> int:
        ...
    
    def __lshift__(self, other):
        ...
    
    def __rshift__(self, other):
        ...
    
    def __and__(self, other):
        ...
    
    def __xor__(self, other):
        ...
    
    def __or__(self, other):
        ...
    
    def __radd__(self, other):
        ...
    
    def __rsub__(self, other):
        ...
    
    def __rmul__(self, other):
        ...
    
    def __rdiv__(self, other):
        ...
    
    def __rtruediv__(self, other): # -> Any:
        ...
    
    def __rfloordiv__(self, other):
        ...
    
    def __rmod__(self, other):
        ...
    
    def __rdivmod__(self, other):
        ...
    
    def __rpow__(self, other, *args): # -> int:
        ...
    
    def __rlshift__(self, other):
        ...
    
    def __rrshift__(self, other):
        ...
    
    def __rand__(self, other):
        ...
    
    def __rxor__(self, other):
        ...
    
    def __ror__(self, other):
        ...
    
    def __iadd__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __isub__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __imul__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __idiv__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __itruediv__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __ifloordiv__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __imod__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __ipow__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __ilshift__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __irshift__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __iand__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __ixor__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __ior__(self, other): # -> Self@ObjectProxy:
        ...
    
    def __neg__(self): # -> Any:
        ...
    
    def __pos__(self): # -> Any:
        ...
    
    def __abs__(self): # -> Any:
        ...
    
    def __invert__(self): # -> Any:
        ...
    
    def __int__(self) -> int:
        ...
    
    def __long__(self):
        ...
    
    def __float__(self): # -> float:
        ...
    
    def __complex__(self): # -> complex:
        ...
    
    def __oct__(self): # -> str:
        ...
    
    def __hex__(self): # -> str:
        ...
    
    def __index__(self): # -> int:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __contains__(self, value): # -> bool:
        ...
    
    def __getitem__(self, key): # -> Any:
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __delitem__(self, key): # -> None:
        ...
    
    def __getslice__(self, i, j): # -> Any:
        ...
    
    def __setslice__(self, i, j, value): # -> None:
        ...
    
    def __delslice__(self, i, j): # -> None:
        ...
    
    def __enter__(self): # -> Any:
        ...
    
    def __exit__(self, *args, **kwargs): # -> Any:
        ...
    
    def __iter__(self): # -> Any:
        ...
    
    def __copy__(self):
        ...
    
    def __deepcopy__(self, memo):
        ...
    
    def __reduce__(self):
        ...
    
    def __reduce_ex__(self, protocol):
        ...
    


class CallableObjectProxy(ObjectProxy):
    def __call__(self, *args, **kwargs): # -> Any:
        ...
    


class PartialCallableObjectProxy(ObjectProxy):
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def __call__(self, *args, **kwargs): # -> Any:
        ...
    


class _FunctionWrapperBase(ObjectProxy):
    __slots__ = ...
    def __init__(self, wrapped, instance, wrapper, enabled=..., binding=..., parent=...) -> None:
        ...
    
    def __get__(self, instance, owner): # -> Any | Self@_FunctionWrapperBase:
        ...
    
    def __call__(self, *args, **kwargs): # -> Any:
        ...
    
    def __set_name__(self, owner, name): # -> None:
        ...
    
    def __instancecheck__(self, instance): # -> bool:
        ...
    
    def __subclasscheck__(self, subclass): # -> bool:
        ...
    


class BoundFunctionWrapper(_FunctionWrapperBase):
    def __call__(self, *args, **kwargs): # -> Any:
        ...
    


class FunctionWrapper(_FunctionWrapperBase):
    __bound_function_wrapper__ = BoundFunctionWrapper
    def __init__(self, wrapped, wrapper, enabled=...) -> None:
        ...
    


def resolve_path(module, name): # -> tuple[ModuleType | Unknown | Any, Unknown, Any]:
    ...

def apply_patch(parent, attribute, replacement): # -> None:
    ...

def wrap_object(module, name, factory, args=..., kwargs=...):
    ...

class AttributeWrapper:
    def __init__(self, attribute, factory, args, kwargs) -> None:
        ...
    
    def __get__(self, instance, owner):
        ...
    
    def __set__(self, instance, value): # -> None:
        ...
    
    def __delete__(self, instance): # -> None:
        ...
    


def wrap_object_attribute(module, name, factory, args=..., kwargs=...): # -> AttributeWrapper:
    ...

def function_wrapper(wrapper): # -> FunctionWrapper:
    ...

def wrap_function_wrapper(module, name, wrapper): # -> FunctionWrapper:
    ...

def patch_function_wrapper(module, name): # -> (wrapper: Unknown) -> FunctionWrapper:
    ...

def transient_function_wrapper(module, name): # -> (wrapper: Unknown) -> FunctionWrapper:
    ...

class WeakFunctionProxy(ObjectProxy):
    __slots__ = ...
    def __init__(self, wrapped, callback=...) -> None:
        ...
    
    def __call__(self, *args, **kwargs): # -> Any:
        ...
    


