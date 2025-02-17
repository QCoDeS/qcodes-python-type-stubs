"""
This type stub file was generated by pyright.
"""

class Status:
    """The Status type defines a logical error model that is suitable for
    different programming environments, including REST APIs and RPC APIs.
    It is used by gRPC.

    :type code: int
    :param code: An enum value of :class: `~google.rpc.Code`.

    :type message: str
    :param message: A developer-facing error message, should be in English.

    :type details: list
    :param details: A list of messages that carry the error details.
                    There is a common set of message types for APIs to use.
                    e.g. [
                            {
                                "@type": string,
                                field1: ...,
                                ...
                            },
                         ]
                    See: https://cloud.google.com/trace/docs/reference/v2/
                         rest/v2/Status#FIELDS.details
    """
    def __init__(self, code, message=..., details=...) -> None:
        ...
    
    @property
    def canonical_code(self): # -> Unknown:
        ...
    
    @property
    def description(self): # -> None:
        ...
    
    @property
    def is_ok(self):
        ...
    
    def format_status_json(self): # -> dict[Unknown, Unknown]:
        """Convert a Status object to json format."""
        ...
    
    @classmethod
    def from_exception(cls, exc): # -> Self@Status:
        ...
    
    @classmethod
    def as_ok(cls): # -> Self@Status:
        ...
    


