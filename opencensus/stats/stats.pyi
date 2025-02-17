"""
This type stub file was generated by pyright.
"""

from opencensus.metrics.export.metric_producer import MetricProducer

class _Stats(MetricProducer):
    """Stats defines a View Manager and a Stats Recorder in order for the
    collection of Stats
    """
    def __init__(self) -> None:
        ...
    
    def get_metrics(self):
        """Get a Metric for each of the view manager's registered views.

        Convert each registered view's associated `ViewData` into a `Metric` to
        be exported, using the current time for metric conversions.

        :rtype: Iterator[:class: `opencensus.metrics.export.metric.Metric`]
        """
        ...
    


stats = ...
