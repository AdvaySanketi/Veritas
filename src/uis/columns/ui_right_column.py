from qt_core import *
import sys


class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        if not RightColumn.objectName():
            RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(0, 40))
        self.label_1.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 20pt; color: yellow; background-color: black;")
        self.label_1.setAlignment(Qt.AlignCenter|Qt.AlignTop)

        self.sep = QWidget(self.menu_1)
        self.sep.setMaximumHeight(15)

        self.label_2 = QLabel(self.menu_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignLeft)
        
        self.label_3 = QLabel(self.menu_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 40))
        self.label_3.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"font-size: 16pt")
        self.label_3.setAlignment(Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 40))
        self.label_4.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font-size: 16pt")
        self.label_4.setAlignment(Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 40))
        self.label_5.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font-size: 16pt")
        self.label_5.setAlignment(Qt.AlignLeft)

        self.sep2 = QWidget(self.menu_1)
        self.sep2.setMaximumHeight(15)

        self.label_6 = QLabel(self.menu_1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 40))
        self.label_6.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font-size: 20pt; color: yellow; background-color: black;")
        self.label_6.setAlignment(Qt.AlignCenter|Qt.AlignTop)

        self.ps = QTextEdit(self.menu_1)
        self.ps.setStyleSheet(u"font-size: 13.2pt; background-color: rgba(0,0,0,0);")
        self.ps.setFrameStyle((QFrame.NoFrame))
        self.ps.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ps.setAlignment(Qt.AlignJustify)
        self.ps.setReadOnly(True)
        self.ps.setPlainText('''
Creating a Program with an Easy to Understand User-Friendly Interface that takes Python Code given as Input by the User and Executes and Displays the Working Mechanism of the Python Code and shows how the Final Output is actually Derived.
This will Help us Better Understand the Working of Various Components of a Python Program and how the Interpreter/Compiler Executes the Program.
        ''')

        self.verticalLayout.addWidget(self.label_1)
        self.verticalLayout.addWidget(self.sep)
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.sep2)
        self.verticalLayout.addWidget(self.label_6)
        self.verticalLayout.addWidget(self.ps)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.menus.addWidget(self.menu_2)

        self.menu_3 = QWidget()
        self.menu_3.setObjectName(u"menu_3")
        self.verticalLayout_3 = QVBoxLayout(self.menu_3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)

        self.menus.addWidget(self.menu_3)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(RightColumn)

        self.menus.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi

    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("LeftColumn", u"Made By", None))
        self.label_2.setText(QCoreApplication.translate("LeftColumn", u"Name: Advay Sanketi", None))
        self.label_3.setText(QCoreApplication.translate("LeftColumn", u"SRN: PES2UG22CS040", None))
        self.label_4.setText(QCoreApplication.translate("LeftColumn", u"Branch: BTech CSE", None))
        self.label_5.setText(QCoreApplication.translate("LeftColumn", u"Sec: E1", None))
        self.label_6.setText(QCoreApplication.translate("LeftColumn", u"Problem Statement", None))
        
    # retranslateUi

