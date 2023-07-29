from qt_core import *

class PyLabel(QLabel):
 
    # constructor
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)

        self.label = QLabel()

        self.label.setWordWrap(True)

        self.label.setStyleSheet("""QLabel{
background-color: black;
margin-top: 0px;
max-width: 30px;
}""")
        self.label.setMinimumWidth(30)
        self.label.setMaximumWidth(50)
        self.label.setMinimumHeight(100)