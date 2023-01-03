"""
This type stub file was generated by pyright.
"""

class AvailableMemoryMetric:
    NAME = ...
    @staticmethod
    def get_value(): # -> int:
        ...
    
    def __call__(self): # -> DerivedLongGauge:
        """ Returns a derived gauge for available memory

        Available memory is defined as memory that can be given instantly to
        processes without the system going into swap.

        :rtype: :class:`opencensus.metrics.export.gauge.DerivedLongGauge`
        :return: The gauge representing the available memory metric
        """
        ...
    


