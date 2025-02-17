"""
This type stub file was generated by pyright.
"""

class Type:
    """
    Indicates whether the message was sent or received.

    Attributes:
      TYPE_UNSPECIFIED (int): Unknown event type.
      SENT (int): Indicates a sent message.
      RECEIVED (int): Indicates a received message.
    """
    TYPE_UNSPECIFIED = ...
    SENT = ...
    RECEIVED = ...


class Annotation:
    """Text annotation with a set of attributes.

    :type timestamp: :class:`~datetime.datetime`
    :param timestamp: The timestamp indicating the time the event occurred.

    :type description: str
    :param description: A user-supplied message describing the event.
                        The maximum length for the description is 256 bytes.

    :type attributes: :class:`~opencensus.trace.attributes.Attributes`
    :param attributes: A set of attributes on the annotation.
                       You can have up to 4 attributes per Annotation.
    """
    def __init__(self, timestamp, description, attributes=...) -> None:
        ...
    
    def format_annotation_json(self): # -> dict[Unknown, Unknown]:
        ...
    


class MessageEvent:
    """An event describing a message sent/received between Spans.

    :type timestamp: :class:`~datetime.datetime`
    :param timestamp: The timestamp indicating the time the event occurred.

    :type type: Enum of :class: `~opencensus.trace.time_event.Type`
    :param type: Indicates whether the message was sent or received.

    :type id: str (int64 format)
    :param id: An identifier for the MessageEvent's message that can be used
               to match SENT and RECEIVED MessageEvents. It is recommended to
               be unique within a Span.

    :type uncompressed_size_bytes: str (int64 format)
    :param uncompressed_size_bytes: The number of uncompressed bytes sent or
                                    received.

    :type compressed_size_bytes: str (int64 format)
    :param compressed_size_bytes: The number of compressed bytes sent or
                                  received. If missing assumed to be the same
                                  size as uncompressed.

    """
    def __init__(self, timestamp, id, type=..., uncompressed_size_bytes=..., compressed_size_bytes=...) -> None:
        ...
    
    def format_message_event_json(self): # -> dict[Unknown, Unknown]:
        ...
    


