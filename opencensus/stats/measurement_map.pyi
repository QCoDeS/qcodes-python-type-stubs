"""
This type stub file was generated by pyright.
"""

logger = ...
class MeasurementMap:
    """Measurement Map is a map from Measures to measured values
    to be recorded at the same time

    :type measure_to_view_map: :class: '~opencensus.stats.measure_to_view_map.
                                        MeasureToViewMap'
    :param measure_to_view_map: the measure to view map that will store the
                                recorded stats with tags

    :type: attachments: dict
    :param attachments: the contextual information about the attachment value.

    """
    def __init__(self, measure_to_view_map, attachments=...) -> None:
        ...
    
    @property
    def measurement_map(self): # -> dict[Unknown, Unknown]:
        """the current measurement map"""
        ...
    
    @property
    def measure_to_view_map(self): # -> Unknown:
        """the current measure to view map for the measurement map"""
        ...
    
    @property
    def attachments(self): # -> dict[Unknown, Unknown] | None:
        """the current contextual information about the attachment value."""
        ...
    
    def measure_int_put(self, measure, value): # -> None:
        """associates the measure of type Int with the given value"""
        ...
    
    def measure_float_put(self, measure, value): # -> None:
        """associates the measure of type Float with the given value"""
        ...
    
    def measure_put_attachment(self, key, value): # -> None:
        """Associate the contextual information of an Exemplar to this MeasureMap
            Contextual information is represented as key - value string pairs.
            If this method is called multiple times with the same key,
            only the last value will be kept.
        """
        ...
    
    def record(self, tags=...): # -> None:
        """records all the measures at the same time with a tag_map.
        tag_map could either be explicitly passed to the method, or implicitly
        read from current runtime context.
        """
        ...
    


