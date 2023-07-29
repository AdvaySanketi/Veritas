from PyQt5.QtCore import QRegExp
from gui.uis.windows import main_window
from qt_core import *

editor = ''
numbar = ''
count = 0
txt = []
editors = []
scroll_lst = []
current_editor = ''
lst = []
lncnt = 1
filename = ''
document = None
override_lines = None

def format(color, style=''):
    _color = QColor()
    if type(color) is not str:
        _color.setRgb(color[0], color[1], color[2])
    else:
        _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format

STYLES = {
    'keyword': format([200, 120, 50]),
    'operator': format([150, 150, 150]),
    'brace': format('darkGray'),
    'defclass': format([0,0,205]),
    'string': format([0,128,0]),
    'string2': format([30, 120, 110]),
    'comment': format([127,255,212]),
    'self': format([150, 85, 140], 'italic'),
    'numbers': format([100, 150, 190]),
    'query': format([30,144,255]),
    'alert': format([178,34,34]),
    'veritas': format([150,0,205]),
}


class PythonHighlighter(QSyntaxHighlighter):


    keywords = [
        'and', 'assert', 'break', 'class', 'continue', 'def',
        'del', 'elif', 'else', 'except', 'exec', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in',
        'is', 'lambda', 'not', 'or', 'pass', 'print',
        'raise', 'return', 'try', 'while', 'yield',
        'None', 'True', 'False',
    ]

    operators = [
        '=',
        '==', '!=', '<', '<=', '>', '>=',
        '\+', '-', '\*', '/', '//', '\%', '\*\*',
        '\+=', '-=', '\*=', '/=', '\%=',
        '\^', '\|', '\&', '\~', '>>', '<<',
    ]

    braces = [
        '\{', '\}', '\(', '\)', '\[', '\]',
    ]

    def __init__(self, text_edit, bar, scrolls, ced, edlst, override=False):
        global filename
        global editor
        global numbar
        global editors
        global current_editor
        global document
        global override_lines
        global scroll_lst
        numbar = bar
        editors = edlst
        scroll_lst = scrolls
        current_editor = ced
        override_lines = override
        editor = text_edit
        document = text_edit.document()

        QSyntaxHighlighter.__init__(self, document)
        
        self.tri_single = (QRegExp("'''"), 1, STYLES['string2'])
        self.tri_double = (QRegExp('"""'), 2, STYLES['string2'])

        rules = []

        rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
                for w in PythonHighlighter.keywords]
        rules += [(r'%s' % o, 0, STYLES['operator'])
                for o in PythonHighlighter.operators]
        rules += [(r'%s' % b, 0, STYLES['brace'])
                for b in PythonHighlighter.braces]

        rules += [
            # 'self'
            (r'\bself\b', 0, STYLES['self']),
            
            # 'veritas'
            (r'\bVeritas\b', 0, STYLES['veritas']),

            # Double-quoted string
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            # Single-quoted string
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),

            # 'def' 
            (r'\bdef\b\s*(\w+)', 1, STYLES['defclass']),
            # 'class'
            (r'\bclass\b\s*(\w+)', 1, STYLES['defclass']),

            # Comment
            (r'#[^\n]*', 0, STYLES['comment']),
            (r'#![^\n]*', 0, STYLES['alert']),
            (r'#\?[^\n]*', 0, STYLES['query']),

            # Numeric literals
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
            
            # Error
            (r'!!.*!!', 0, STYLES['alert']),
            
        ]

        self.rules = [(QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]
        
        

    def highlightBlock(self, text):
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        try:
            if override_lines == False:
                self.indent()
        except IndexError:
            pass

        global filename
        for i in editors:
            if i[0] == current_editor:
                if override_lines == False:
                    if i[1] == "Untitled.py":
                        filename = None
                        self.lnum_new()
                    else:
                        filename = i[1]
                        self.linenumbers()
        
        if override_lines == False:
            current_editor.cursorPositionChanged.connect(self.lnum_new)

    def indent(self):
        global txt
        txt.append(current_editor.textCursor().block().text())
        text = txt[len(txt)-3]
        count = text.count('\t')
        if current_editor.toPlainText().endswith(':\n'):
            if text.startswith('\t'):
                current_editor.insertPlainText('\t'*(count+1))
            else:
                current_editor.insertPlainText('\t')
    
    def linenumbers(self):
        text = ''
        with open(filename, 'r') as file:
            data = file.readlines()
        nlines = len(data)
        for i in range(1, nlines+1):
            if i == (current_editor.textCursor().blockNumber() + 1) :
                text = text + str(i) + ' 📌' + '\n'
            else:
                text = text + str(i) + '\n'
            numbar.setMinimumWidth(30 + 10*len(str(i)))
        numbar.setText(text)
        if current_editor.textCursor().blockNumber() >= nlines-1:
            self.lnum_new()
    
    def lnum_new(self):
        text = ''
        for i in range(1, current_editor.document().blockCount()+1):
            if i == (current_editor.textCursor().blockNumber() + 1) :
                text = text + str(i) + ' 📌' + '\n'
            else:
                text = text + str(i) + '\n'
            numbar.setMinimumWidth(30 + 10*len(str(i)))
        
        numbar.setText(text)


    def match_multiline(self, text, delimiter, in_state, style):
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        else:
            start = delimiter.indexIn(text)
            add = delimiter.matchedLength()
            
        while start >= 0:
            end = delimiter.indexIn(text, start + add)
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            self.setFormat(start, length, style)
            start = delimiter.indexIn(text, start + length)

        if self.currentBlockState() == in_state:
            return True
        else:
            return False