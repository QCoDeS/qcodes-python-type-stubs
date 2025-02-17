"""
This type stub file was generated by pyright.
"""

from .wrappers import BoundFunctionWrapper, CallableObjectProxy, FunctionWrapper, ObjectProxy, PartialCallableObjectProxy, WeakFunctionProxy, apply_patch, function_wrapper, patch_function_wrapper, resolve_path, transient_function_wrapper, wrap_function_wrapper, wrap_object, wrap_object_attribute
from .decorators import AdapterFactory, adapter_factory, decorator, synchronized
from .importer import discover_post_import_hooks, notify_module_loaded, register_post_import_hook, when_imported
from inspect import getcallargs
from .arguments import formatargspec

__version_info__ = ...
__version__ = ...

__all__ = ["formatargspec",
"AdapterFactory",
"adapter_factory",
"decorator",
"synchronized",
    "discover_post_import_hooks",
    "notify_module_loaded",
    "register_post_import_hook",
    "when_imported",
    "BoundFunctionWrapper",
    "CallableObjectProxy",
    "FunctionWrapper",
    "ObjectProxy",
    "PartialCallableObjectProxy",
    "WeakFunctionProxy",
    "apply_patch",
    "function_wrapper",
    "patch_function_wrapper",
    "resolve_path",
    "transient_function_wrapper",
    "wrap_function_wrapper",
    "wrap_object",
    "wrap_object_attribute",]