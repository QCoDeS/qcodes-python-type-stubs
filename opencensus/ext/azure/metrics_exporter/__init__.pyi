"""
This type stub file was generated by pyright.
"""

import atexit
from opencensus.common import utils as common_utils
from opencensus.ext.azure.common import Options, utils
from opencensus.ext.azure.common.processor import ProcessorMixin
from opencensus.ext.azure.common.protocol import Data, DataPoint, Envelope, MetricData
from opencensus.ext.azure.common.storage import LocalFileStorage
from opencensus.ext.azure.common.transport import TransportMixin, TransportStatusCode
from opencensus.ext.azure.metrics_exporter import standard_metrics
from opencensus.ext.azure.statsbeat.statsbeat_metrics import _NETWORK_STATSBEAT_NAMES
from opencensus.metrics import transport
from opencensus.metrics.export.metric_descriptor import MetricDescriptorType
from opencensus.stats import stats as stats_module

__all__ = ['MetricsExporter', 'new_metrics_exporter']
class MetricsExporter(TransportMixin, ProcessorMixin):
    """Metrics exporter for Microsoft Azure Monitor."""
    def __init__(self, is_stats=..., **options) -> None:
        ...
    
    def export_metrics(self, metrics): # -> None:
        ...
    
    def metric_to_envelopes(self, metric): # -> list[Unknown]:
        ...
    
    def shutdown(self): # -> None:
        ...
    


def new_metrics_exporter(**options): # -> MetricsExporter:
    ...

