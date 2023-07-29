from qt_core import *

class ScrollMessageBox(QMessageBox):
   def __init__(self, l, *args, **kwargs):
      QMessageBox.__init__(self, *args, **kwargs)
      scroll = QScrollArea(self)
      scroll.setWidgetResizable(True)
      self.content = QWidget()
      scroll.setWidget(self.content)
      lay = QVBoxLayout(self.content)
      for item in l:
         lay.addWidget(QLabel(item, self))
      self.layout().addWidget(scroll, 0, 0, 1, self.layout().columnCount())
      self.setStyleSheet("QScrollArea{min-width:300 px; min-height: 400px}")
