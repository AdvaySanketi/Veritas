# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesMnpIiK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from gui.uis.windows import main_window
from gui.uis.windows.main_window.functions_main_window import MainFunctions
from qt_core import *
from gui.uis.windows.main_window import *
import gui.core.synlight as synlight
from main import data, filename

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.pages.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(200)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(10, 40, 5, 5)
        self.logo = QFrame(self.page_1)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(700, 500))
        self.logo.setMaximumSize(QSize(700, 500))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        
        self.image = QLabel(self.page_1)
        self.pixmap = QPixmap("gui\images\svg_images\Tejas_logo.png")
        self.image.setPixmap(self.pixmap)
        self.image.setMinimumSize(QSize(700, 600))
        self.image.setStyleSheet(u"padding-top : 0px; padding-left : 300px; padding-right : 350px;")
        self.image.setScaledContents(True)
        self.page_1_layout.addWidget(self.image)
        
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size: 70pt;padding-bottom : 100px;padding-left: 450px; color: yellow")

        self.pages.addWidget(self.page_1)

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QFrame {\n"
"	font-size: 18pt;\n"
"}")
        self.page_2_Layout = QVBoxLayout(self.page_2)
        self.page_2_Layout.setObjectName(u"page_2_Layout")
        self.tabs = QTabWidget(self.page_2)
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)
        self.tabs.setMovable(True)
        self.tabs.setStyleSheet('''QTabBar::tab { background: gray; color: white; padding: 10px; max-height: 20px; min-width: 150px;}
QTabBar::tab:selected { background: Black; color: white; font-size: 12pt; margin-left: -4px; margin-right: -4px;}
QTabBar::tab:!selected { margin-top: 6px; color: white; font-size: 12pt;}
QTabBar::tab:first:selected { margin-left: 0; }
QTabBar::tab:last:selected { margin-right: 0; }
QTabBar::tab:only-one { margin: 0; }
QTabWidget { border: none; }
QWidget { background: black; }
QTabBar { qproperty-drawBase: 0; background: transparent; } ''')

        self.editors = []
        self.scrolls = []
        self.current_editor = ''

        self.tabs.tabCloseRequested.connect(self.remove)
        self.tabs.currentChanged.connect(self.change)

        self.pages.addWidget(self.page_2)

        self.main_pages_layout.addWidget(self.pages)        


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))

    # retranslateUi

    def remove(self, index):
        self.tabs.removeTab(index)
        if index < (len(self.editors)):
            del self.editors[index]
            self.change(self.tabs.currentIndex())

    def change(self, index):
        if index < (len(self.editors)):
            try:
                self.current_editor = self.editors[index][0]
                if self.editors[index][0] == None:
                    pass
                elif self.editors[index][2] != None:
                    highlight = synlight.PythonHighlighter(self.current_editor, self.editors[index][2], self.scrolls, self.current_editor, self.editors)
            except IndexError:
                self.editors = []

