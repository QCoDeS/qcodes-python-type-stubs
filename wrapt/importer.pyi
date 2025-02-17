"""
This type stub file was generated by pyright.
"""

import threading
from importlib.util import find_spec
from .decorators import synchronized

"""This module implements a post import hook mechanism styled after what is
described in PEP-369. Note that it doesn't cope with modules being reloaded.

"""
PY2 = ...
if PY2:
    string_types = ...
    find_spec = ...
else:
    string_types = ...
_post_import_hooks = ...
_post_import_hooks_init = ...
_post_import_hooks_lock = threading.RLock()
@synchronized(_post_import_hooks_lock)
def register_post_import_hook(hook, name): # -> None:
    ...

def discover_post_import_hooks(group): # -> None:
    ...

@synchronized(_post_import_hooks_lock)
def notify_module_loaded(module): # -> None:
    ...

class _ImportHookLoader:
    def load_module(self, fullname): # -> ModuleType:
        ...
    


class _ImportHookChainedLoader:
    def __init__(self, loader) -> None:
        ...
    


class ImportHookFinder:
    def __init__(self) -> None:
        ...
    
    @synchronized(_post_import_hooks_lock)
    def find_module(self, fullname, path=...): # -> _ImportHookLoader | _ImportHookChainedLoader | None:
        ...
    
    def find_spec(self, fullname, path=..., target=...): # -> ModuleSpec | None:
        ...
    


def when_imported(name): # -> (hook: Unknown) -> Unknown:
    ...

