



# IMPORT QT CORE

from qt_core import *

# STYLE

style = '''
QPlainTextEdit {{
	background-color: {_bg_color};
	border-radius: {_radius}px;
	border: {_border_size}px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {_selection_color};
	selection-background-color: {_context_color};
    color: {_color};
}}
QPlainTextEdit:focus {{
	border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
'''

# PY PUSH BUTTON

class PyPlainEdit(QPlainTextEdit):
    def __init__(
        self, 
        text = "",
        place_holder_text = "",
        radius = 8,
        border_size = 2,
        color = "#000",
        selection_color = "#000",
        bg_color = "#333",
        bg_color_active = "#222",
        context_color = "#000"
    ):
        super().__init__()

        # PARAMETERS
        if text:
            self.setPlainText(text)
        if place_holder_text:
            self.setPlaceholderText(place_holder_text)

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            border_size,
            color,
            selection_color,
            bg_color,
            bg_color_active,
            context_color
        )

    # SET STYLESHEET
    def set_stylesheet(
        self,
        radius,
        border_size,
        color,
        selection_color,
        bg_color,
        bg_color_active,
        context_color
    ):
        _background_color = "Background-color"
        # APPLY STYLESHEET
        style_format = style.format(
            _background_color = "rgba(0, 0, 0,0)",
            _radius = radius,
            _border_size = border_size,           
            _color = color,
            _selection_color = selection_color,
            _bg_color = bg_color,
            _bg_color_active = bg_color_active,
            _context_color = context_color
        )
        self.setStyleSheet(style_format)