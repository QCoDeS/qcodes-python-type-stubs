"""
This type stub file was generated by pyright.
"""

logger = ...
class ProcessorMixin:
    """ProcessorMixin adds the ability to process telemetry processors

    Telemetry processors are functions that are called before exporting of
    telemetry to possibly modify the envelope contents.
    """
    def add_telemetry_processor(self, processor): # -> None:
        """Adds telemetry processor to the collection. Telemetry processors
        will be called one by one before telemetry item is pushed for sending
        and in the order they were added.

        :param processor: The processor to add.
        """
        ...
    
    def clear_telemetry_processors(self): # -> None:
        """Removes all telemetry processors"""
        ...
    
    def apply_telemetry_processors(self, envelopes): # -> list[Unknown]:
        """Applies all telemetry processors in the order they were added.

        This function will return the list of envelopes to be exported after
        each processor has been run sequentially. Individual processors can
        throw exceptions and fail, but the applying of all telemetry processors
        will proceed (not fast fail). Processors also return True if envelope
        should be included for exporting, False otherwise.

        :param envelopes: The envelopes to apply each processor to.
        """
        ...
    


