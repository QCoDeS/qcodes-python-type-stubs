"""
This type stub file was generated by pyright.
"""

import logging
import random
import threading
import time
import traceback
from opencensus.common.schedule import Queue, QueueEvent, QueueExitEvent
from opencensus.ext.azure.common import Options, utils
from opencensus.ext.azure.common.processor import ProcessorMixin
from opencensus.ext.azure.common.protocol import Data, Envelope, Event, ExceptionData, Message
from opencensus.ext.azure.common.storage import LocalFileStorage
from opencensus.ext.azure.common.transport import TransportMixin, TransportStatusCode
from opencensus.ext.azure.statsbeat import statsbeat
from opencensus.trace import execution_context

logger = ...
__all__ = ['AzureEventHandler', 'AzureLogHandler']
class BaseLogHandler(logging.Handler):
    def __init__(self, **options) -> None:
        ...
    
    def close(self, timeout=...): # -> None:
        ...
    
    def createLock(self): # -> None:
        ...
    
    def emit(self, record): # -> None:
        ...
    
    def log_record_to_envelope(self, record):
        ...
    
    def flush(self, timeout=...): # -> None:
        ...
    


class Worker(threading.Thread):
    daemon = ...
    def __init__(self, src, dst) -> None:
        ...
    
    def run(self): # -> None:
        ...
    
    def stop(self, timeout=...): # -> float | None:
        ...
    


class SamplingFilter(logging.Filter):
    def __init__(self, probability=...) -> None:
        ...
    
    def filter(self, record): # -> bool:
        ...
    


class AzureLogHandler(BaseLogHandler, TransportMixin, ProcessorMixin):
    """Handler for logging to Microsoft Azure Monitor."""
    def __init__(self, **options) -> None:
        ...
    
    def log_record_to_envelope(self, record): # -> Envelope:
        ...
    


class AzureEventHandler(TransportMixin, ProcessorMixin, BaseLogHandler):
    """Handler for sending custom events to Microsoft Azure Monitor."""
    def __init__(self, **options) -> None:
        ...
    
    def log_record_to_envelope(self, record): # -> Envelope:
        ...
    


def create_envelope(instrumentation_key, record): # -> Envelope:
    ...

