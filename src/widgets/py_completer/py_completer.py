from qt_core import *

class PyCompleter(QCompleter):
    insertText = Signal(str)

    def __init__(self, myKeywords=None,parent=None):
        with open("gui/core/wordlst.txt", 'r') as file:
            myKeywords = file.readlines()
        
        myKeywords = list(set(myKeywords))

        QCompleter.__init__(self, myKeywords, parent)
        self.activated.connect(self.changeCompletion)

    def changeCompletion(self, completion):
        if completion.find("(") != -1:
            completion = completion[:completion.find("(")]
        self.insertText.emit(completion)