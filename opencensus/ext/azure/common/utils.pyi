"""
This type stub file was generated by pyright.
"""

azure_monitor_context = ...
def microseconds_to_duration(microseconds): # -> LiteralString:
    ...

def timestamp_to_duration(start_time, end_time): # -> LiteralString:
    ...

def timestamp_to_iso_str(timestamp): # -> str:
    ...

uuid_regex_pattern = ...
def validate_instrumentation_key(instrumentation_key): # -> None:
    """Validates the instrumentation key used for Azure Monitor.

    An instrumentation key cannot be null or empty. An instrumentation key
    is valid for Azure Monitor only if it is a valid UUID.

    :param instrumentation_key: The instrumentation key to validate
    """
    ...

