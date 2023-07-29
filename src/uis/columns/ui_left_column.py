from qt_core import *


class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):
        if not LeftColumn.objectName():
            LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(5)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5,5,5,5)
        self.menus = QStackedWidget(LeftColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1,1,1,1)
        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(0, 40))
        self.label_1.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 20pt")
        self.label_1.setAlignment(Qt.AlignCenter|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label_1)

        self.btn_1_widget = QWidget(self.menu_1)
        self.btn_1_widget.setObjectName(u"btn_1_widget")
        self.btn_1_widget.setMinimumSize(QSize(0, 60))
        self.btn_1_widget.setMaximumSize(QSize(16777215, 90))
        self.btn_1_layout = QHBoxLayout(self.btn_1_widget)
        self.btn_1_layout.setSpacing(0)
        self.btn_1_layout.setObjectName(u"btn_1_layout")
        self.btn_1_layout.setContentsMargins(0, 0, 0, 0)

        self.autolabel = QLabel(self.menu_1)
        self.autolabel.setObjectName(u"autolabel")
        self.autolabel.setMinimumSize(QSize(0, 40))
        self.autolabel.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        self.autolabel.setFont(font)
        self.autolabel.setStyleSheet(u"font-size: 14pt")
        self.btn_1_layout.addWidget(self.autolabel)

        self.verticalLayout.addWidget(self.btn_1_widget)

        self.btn_2_widget = QWidget(self.menu_1)
        self.btn_2_widget.setObjectName(u"btn_2_widget")
        self.btn_2_widget.setMinimumSize(QSize(0, 60))
        self.btn_2_widget.setMaximumSize(QSize(16777215, 90))
        self.btn_2_layout = QHBoxLayout(self.btn_2_widget)
        self.btn_2_layout.setSpacing(0)
        self.btn_2_layout.setObjectName(u"btn_2_layout")
        self.btn_2_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_2_widget)

        self.btn_3_widget = QWidget(self.menu_1)
        self.btn_3_widget.setObjectName(u"btn_3_widget")
        self.btn_3_widget.setMinimumSize(QSize(0, 60))
        self.btn_3_widget.setMaximumSize(QSize(16777215, 90))
        self.btn_3_layout = QHBoxLayout(self.btn_3_widget)
        self.btn_3_layout.setSpacing(0)
        self.btn_3_layout.setObjectName(u"btn_3_layout")
        self.btn_3_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_3_widget)

        self.btn_4_widget = QWidget(self.menu_1)
        self.btn_4_widget.setObjectName(u"btn_4_widget")
        self.btn_4_widget.setMinimumSize(QSize(0, 60))
        self.btn_4_widget.setMaximumSize(QSize(16777215, 90))
        self.btn_4_layout = QHBoxLayout(self.btn_4_widget)
        self.btn_4_layout.setSpacing(0)
        self.btn_4_layout.setObjectName(u"btn_4_layout")
        self.btn_4_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_4_widget)

        self.btn_5_widget = QWidget(self.menu_1)
        self.btn_5_widget.setObjectName(u"btn_5_widget")
        self.btn_5_widget.setMinimumSize(QSize(0, 60))
        self.btn_5_widget.setMaximumSize(QSize(16777215, 90))
        self.btn_5_layout = QVBoxLayout(self.btn_5_widget)
        self.btn_5_layout.setSpacing(0)
        self.btn_5_layout.setObjectName(u"btn_5_layout")
        self.btn_5_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.btn_5_widget)

        self.menus.addWidget(self.menu_1)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("LeftColumn", u"Settings Tab", None))
        self.autolabel.setText(QCoreApplication.translate("LeftColumn", u"AutoCompletion", None))

    # retranslateUi

