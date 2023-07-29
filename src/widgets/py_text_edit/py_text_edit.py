



# IMPORT QT CORE

from gui.uis.windows import main_window
from qt_core import *

toggle_btn = None
flag = ''

# STYLE

style = '''
QTextEdit {{
	background-color: {_bg_color};
	border-radius: {_radius}px;
	border: {_border_size}px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {_selection_color};
	selection-background-color: {_context_color};
    color: {_color};
}}
QTextEdit:focus {{
	border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
'''

# PY PUSH BUTTON

class PyTextEdit(QTextEdit):
    def __init__(
        self,
        t_btn = None,
        flag_check = True,
        text = "",
        place_holder_text = "",
        radius = 8,
        border_size = 2,
        color = "#000",
        selection_color = "#000",
        bg_color = "#333",
        bg_color_active = "#222",
        context_color = "#000",
        *args
    ):
        global toggle_btn
        global flag

        QTextEdit.__init__(self, *args)
        self.completer = None
        toggle_btn = t_btn
        if flag_check != True:
            flag = flag_check

        if text:
            self.setText(text)
        if place_holder_text:
            self.setPlaceholderText(place_holder_text)

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
    
    def setCompleter(self, completer):
        if self.completer:
            self.disconnect(self.completer, 0, self, 0)
        if not completer:
            return

        completer.setWidget(self)
        completer.setCompletionMode(QCompleter.PopupCompletion)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer = completer
        self.completer.activated.connect(self.insertCompletion)

    def insertCompletion(self, completion):
        tc = self.textCursor()
        extra = (len(completion) - len(self.completer.completionPrefix()))
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:-1])
        self.setTextCursor(tc)

    def get_completer(self):
        return self.completer

    def disconnect(self):
        self.disconnect(self.completer, 0, self, 0)

    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)
        return tc.selectedText()

    def focusInEvent(self, event):
        if self.completer:
            self.completer.setWidget(self)
        QTextEdit.focusInEvent(self, event)

    def keyPressEvent(self, event):
        global toggle_btn
        if (self.completer == None and flag == "input"):
            return

        if self.completer and self.completer.popup() and self.completer.popup().isVisible():
            if event.key() in (
            Qt.Key_Enter,
            Qt.Key_Return,
            Qt.Key_Escape,
            Qt.Key_Tab,
            Qt.Key_Backtab):
                event.ignore()
                return

        isShortcut = (event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Space)

        if (not self.completer or not isShortcut):
            pass
            QTextEdit.keyPressEvent(self, event)

        ctrlOrShift = event.modifiers() in (Qt.ControlModifier, Qt.ShiftModifier)
        if ctrlOrShift and event.text()== '':
            return

        eow = "~!@#$%^&*+{}|:\"<>?,./;'[]\\-="

        hasModifier = ((event.modifiers() != Qt.NoModifier) and not ctrlOrShift)

        completionPrefix = self.textUnderCursor()

        if not isShortcut and (hasModifier or len(event.text()) == 0 or len(completionPrefix) < 1 or event.text()[-1] in eow):
            self.completer.popup().hide()
            return

        self.completer.setCompletionPrefix(completionPrefix)
        popup = self.completer.popup()
        popup.setCurrentIndex(self.completer.completionModel().index(0,0))
        if toggle_btn != None:
            if toggle_btn.isChecked():
                cr = self.cursorRect()
                cr.setWidth(self.completer.popup().sizeHintForColumn(0) + self.completer.popup().verticalScrollBar().sizeHint().width())
                self.completer.complete(cr)