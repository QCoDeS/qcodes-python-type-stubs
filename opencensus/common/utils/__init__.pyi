"""
This type stub file was generated by pyright.
"""

import calendar
import datetime
import weakref

UTF8 = ...
MAX_LENGTH = ...
ISO_DATETIME_REGEX = ...
def get_truncatable_str(str_to_convert): # -> dict[str, Unknown]:
    """Truncate a string if exceed limit and record the truncated bytes
    count.
    """
    ...

def check_str_length(str_to_check, limit=...): # -> tuple[str, int]:
    """Check the length of a string. If exceeds limit, then truncate it.

    :type str_to_check: str
    :param str_to_check: String to check.

    :type limit: int
    :param limit: The upper limit of the length.

    :rtype: tuple
    :returns: The string it self if not exceeded length, or truncated string
              if exceeded and the truncated byte count.
    """
    ...

def to_iso_str(ts=...): # -> str:
    """Get an ISO 8601 string for a UTC datetime."""
    ...

def timestamp_to_microseconds(timestamp): # -> float:
    """Convert a timestamp string into a microseconds value
    :param timestamp
    :return time in microseconds
    """
    ...

def iuniq(ible): # -> Generator[Unknown, None, None]:
    """Get an iterator over unique items of `ible`."""
    ...

def uniq(ible): # -> list[Unknown]:
    """Get a list of unique items of `ible`."""
    ...

def window(ible, length): # -> Generator[list[Unknown], None, None]:
    """Split `ible` into multiple lists of length `length`.

    >>> list(window(range(5), 2))
    [[0, 1], [2, 3], [4]]
    """
    ...

def get_weakref(func): # -> ref | WeakMethod[Unknown] | WeakMethod:
    """Get a weak reference to bound or unbound `func`.

    If `func` is unbound (i.e. has no __self__ attr) get a weakref.ref,
    otherwise get a wrapper that simulates weakref.ref.
    """
    ...

