from qt_core import *

class PyMessageLabel(QLabel):

    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        self.label = QLabel()

        self.label.setWordWrap(True)

        self.label.setStyleSheet("""QLabel{
background-color: black;
border-radius: 20px;
}""")
        self.label.setMinimumWidth(30)
        self.label.setMaximumWidth(100)
        self.label.setMinimumHeight(30)
        self.label.setMaximumHeight(50)