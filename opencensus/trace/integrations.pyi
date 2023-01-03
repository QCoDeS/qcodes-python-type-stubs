"""
This type stub file was generated by pyright.
"""

_INTEGRATIONS_BIT_MASK = ...
_INTEGRATIONS_LOCK = ...
class _Integrations:
    NONE = ...
    DJANGO = ...
    FLASK = ...
    GOOGLE_CLOUD = ...
    HTTP_LIB = ...
    LOGGING = ...
    MYSQL = ...
    POSTGRESQL = ...
    PYMONGO = ...
    PYMYSQL = ...
    PYRAMID = ...
    REQUESTS = ...
    SQLALCHEMY = ...


def get_integrations(): # -> Literal[0]:
    ...

def add_integration(integration): # -> None:
    ...

def remove_intregration(integration): # -> None:
    ...

