"""
This type stub file was generated by pyright.
"""

from opencensus.trace import base_span

MAX_NUM_ATTRIBUTES = ...
MAX_NUM_ANNOTATIONS = ...
MAX_NUM_MESSAGE_EVENTS = ...
MAX_NUM_LINKS = ...
class BoundedList(Sequence):
    """An append only list with a fixed max size."""
    def __init__(self, maxlen) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __getitem__(self, index):
        ...
    
    def __len__(self): # -> int:
        ...
    
    def __iter__(self): # -> Iterator[Unknown]:
        ...
    
    def append(self, item): # -> None:
        ...
    
    def extend(self, seq): # -> None:
        ...
    
    @classmethod
    def from_seq(cls, maxlen, seq): # -> Self@BoundedList:
        ...
    


class BoundedDict(MutableMapping):
    """A dict with a fixed max capacity."""
    def __init__(self, maxlen) -> None:
        ...
    
    def __repr__(self): # -> str:
        ...
    
    def __getitem__(self, key):
        ...
    
    def __setitem__(self, key, value): # -> None:
        ...
    
    def __delitem__(self, key): # -> None:
        ...
    
    def __iter__(self): # -> Iterator[Unknown]:
        ...
    
    def __len__(self): # -> int:
        ...
    
    @classmethod
    def from_map(cls, maxlen, mapping): # -> Self@BoundedDict:
        ...
    


class SpanKind:
    UNSPECIFIED = ...
    SERVER = ...
    CLIENT = ...


class Span(base_span.BaseSpan):
    """A span is an individual timed event which forms a node of the trace
    tree. Each span has its name, span id and parent id. The parent id
    indicates the causal relationships between the individual spans in a
    single distributed trace. Span that does not have a parent id is called
    root span. All spans associated with a specific trace also share a common
    trace id. Spans do not need to be continuous, there can be gaps between
    two spans.

    :type name: str
    :param name: The name of the span.

    :type parent_span: :class:`~opencensus.trace.span.Span`
    :param parent_span: (Optional) Parent span.

    :type attributes: dict
    :param attributes: Collection of attributes associated with the span.
                   Attribute keys must be less than 128 bytes.
                   Attribute values must be less than 16 kilobytes.

    :type start_time: str
    :param start_time: (Optional) Start of the time interval (inclusive)
                       during which the trace data was collected from the
                       application.

    :type end_time: str
    :param end_time: (Optional) End of the time interval (inclusive) during
                     which the trace data was collected from the application.

    :type span_id: int
    :param span_id: Identifier for the span, unique within a trace.

    :type stack_trace: :class: `~opencensus.trace.stack_trace.StackTrace`
    :param stack_trace: (Optional) A call stack appearing in a trace

    :type annotations: list(:class:`opencensus.trace.time_event.Annotation`)
    :param annotations: (Optional) The list of span annotations.

    :type message_events:
        list(:class:`opencensus.trace.time_event.MessageEvent`)
    :param message_events: (Optional) The list of span message events.

    :type links: list
    :param links: (Optional) Links associated with the span. You can have up
                  to 128 links per Span.

    :type status: :class: `~opencensus.trace.status.Status`
    :param status: (Optional) An optional final status for this span.

    :type same_process_as_parent_span: bool
    :param same_process_as_parent_span: (Optional) A highly recommended but not
                                        required flag that identifies when a
                                        trace crosses a process boundary.
                                        True when the parent_span belongs to
                                        the same process as the current span.

    :type context_tracer: :class:`~opencensus.trace.tracers.context_tracer.
                                 ContextTracer`
    :param context_tracer: The tracer that holds a stack of spans. If this is
                           not None, then when exiting a span, use the end_span
                           method in the tracer class to finish a span. If no
                           tracer is passed in, then just finish the span using
                           the finish method in the Span class.

    :type span_kind: int
    :param span_kind: (Optional) Highly recommended flag that denotes the type
                        of span (valid values defined by :class:
                        `opencensus.trace.span.SpanKind`)
    """
    def __init__(self, name, parent_span=..., attributes=..., start_time=..., end_time=..., span_id=..., stack_trace=..., annotations=..., message_events=..., links=..., status=..., same_process_as_parent_span=..., context_tracer=..., span_kind=...) -> None:
        ...
    
    _on_create_callbacks = ...
    @staticmethod
    def on_create(callback): # -> None:
        ...
    
    @property
    def children(self): # -> list[Unknown]:
        """The child spans of the current span."""
        ...
    
    def span(self, name=...): # -> Span:
        """Create a child span for the current span and append it to the child
        spans list.

        :type name: str
        :param name: (Optional) The name of the child span.

        :rtype: :class: `~opencensus.trace.span.Span`
        :returns: A child Span to be added to the current span.
        """
        ...
    
    def add_attribute(self, attribute_key, attribute_value): # -> None:
        """Add attribute to span.

        :type attribute_key: str
        :param attribute_key: Attribute key.

        :type attribute_value:str
        :param attribute_value: Attribute value.
        """
        ...
    
    def add_annotation(self, description, **attrs): # -> None:
        """Add an annotation to span.

        :type description: str
        :param description: A user-supplied message describing the event.
                        The maximum length for the description is 256 bytes.

        :type attrs: kwargs
        :param attrs: keyworded arguments e.g. failed=True, name='Caching'
        """
        ...
    
    def add_message_event(self, message_event): # -> None:
        """Add a message event to this span.

        :type message_event: :class:`opencensus.trace.time_event.MessageEvent`
        :param message_event: The message event to attach to this span.
        """
        ...
    
    def add_link(self, link): # -> None:
        """Add a Link.

        :type link: :class: `~opencensus.trace.link.Link`
        :param link: A Link object.
        """
        ...
    
    def set_status(self, status): # -> None:
        """Sets span status.

        :type code: :class: `~opencensus.trace.status.Status`
        :param code: A Status object.
        """
        ...
    
    def start(self): # -> None:
        """Set the start time for a span."""
        ...
    
    def finish(self): # -> None:
        """Set the end time for a span."""
        ...
    
    def __iter__(self): # -> Generator[Any | Self@Span, None, None]:
        """Iterate through the span tree."""
        ...
    
    def __enter__(self): # -> Self@Span:
        """Start a span."""
        ...
    
    def __exit__(self, exception_type, exception_value, traceback): # -> None:
        """Finish a span."""
        ...
    


def format_span_json(span): # -> dict[str, Unknown]:
    """Helper to format a Span in JSON format.

    :type span: :class:`~opencensus.trace.span.Span`
    :param span: A Span to be transferred to JSON format.

    :rtype: dict
    :returns: Formatted Span.
    """
    ...

