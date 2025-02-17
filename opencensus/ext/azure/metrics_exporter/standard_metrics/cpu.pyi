"""
This type stub file was generated by pyright.
"""

class ProcessorTimeMetric:
    NAME = ...
    @staticmethod
    def get_value():
        ...
    
    def __call__(self): # -> DerivedDoubleGauge:
        """ Returns a derived gauge for the processor time.

        Processor time is defined as a float representing the current system
        wide CPU utilization minus idle CPU time as a percentage. Idle CPU
        time is defined as the time spent doing nothing. Return values range
        from 0.0 to 100.0 inclusive.

        :rtype: :class:`opencensus.metrics.export.gauge.DerivedDoubleGauge`
        :return: The gauge representing the processor time metric
        """
        ...
    


