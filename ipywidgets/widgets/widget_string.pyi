"""
This type stub file was generated by pyright.
"""

from .widget_description import DescriptionStyle, DescriptionWidget
from .valuewidget import ValueWidget
from .widget import register
from .widget_core import CoreWidget

"""String class.

Represents a unicode string using a widget.
"""
class _StringStyle(DescriptionStyle, CoreWidget):
    """Text input style widget."""
    _model_name = ...
    background = ...
    font_size = ...
    text_color = ...


@register
class LabelStyle(_StringStyle):
    """Label style widget."""
    _model_name = ...
    font_family = ...
    font_style = ...
    font_variant = ...
    font_weight = ...
    text_decoration = ...


@register
class TextStyle(_StringStyle):
    """Text input style widget."""
    _model_name = ...


@register
class HTMLStyle(_StringStyle):
    """HTML style widget."""
    _model_name = ...


@register
class HTMLMathStyle(_StringStyle):
    """HTML with math style widget."""
    _model_name = ...


class _String(DescriptionWidget, ValueWidget, CoreWidget):
    """Base class used to create widgets that represent a string."""
    value = ...
    placeholder = ...
    style = ...
    def __init__(self, value=..., **kwargs) -> None:
        ...
    
    _model_name = ...


@register
class HTML(_String):
    """Renders the string `value` as HTML."""
    _view_name = ...
    _model_name = ...
    style = ...


@register
class HTMLMath(_String):
    """Renders the string `value` as HTML, and render mathematics."""
    _view_name = ...
    _model_name = ...
    style = ...


@register
class Label(_String):
    """Label widget.

    It also renders math inside the string `value` as Latex (requires $ $ or
    $$ $$ and similar latex tags).
    """
    _view_name = ...
    _model_name = ...
    style = ...


@register
class Textarea(_String):
    """Multiline text area widget."""
    _view_name = ...
    _model_name = ...
    rows = ...
    disabled = ...
    continuous_update = ...
    style = ...


@register
class Text(_String):
    """Single line textbox widget."""
    _view_name = ...
    _model_name = ...
    disabled = ...
    continuous_update = ...
    style = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def on_submit(self, callback, remove=...): # -> None:
        """(Un)Register a callback to handle text submission.

        Triggered when the user clicks enter.

        Parameters
        ----------
        callback: callable
            Will be called with exactly one argument: the Widget instance
        remove: bool (optional)
            Whether to unregister the callback
        """
        ...
    


@register
class Password(Text):
    """Single line textbox widget."""
    _view_name = ...
    _model_name = ...
    disabled = ...


@register
class Combobox(Text):
    """Single line textbox widget with a dropdown and autocompletion.
    """
    _model_name = ...
    _view_name = ...
    options = ...
    ensure_option = ...


