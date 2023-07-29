import json
from gui.widgets.py_scroll_area.py_scroll_area import PyScrollArea
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
import random
import subprocess
from qt_core import *
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from gui.widgets import *
from . ui_main import *
import gui.core.synlight as synlight
from main import data, filename
from threading import *
from gui.core.visualize import visualize, visualizer
from gui.core.terminal import get_state

user_id = ''
count3 = 0

class SetupMainWindow:
    def __init__(self):
        super().__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_editor.png",
            "btn_id" : "btn_editor",
            "btn_text" : "Editors",
            "btn_tooltip" : "Open Editors",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_run.png",
            "btn_id" : "btn_run",
            "btn_text" : "Run the Program",
            "btn_tooltip" : "Run Program",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_flowchart.png",
            "btn_id" : "btn_flowchart",
            "btn_text" : "Create Program Flowchart",
            "btn_tooltip" : "Create Program Flowchart",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_file.svg",
            "btn_id" : "btn_new_file",
            "btn_text" : "New File",
            "btn_tooltip" : "Create new file",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_folder_open.svg",
            "btn_id" : "btn_open_file",
            "btn_text" : "Open File",
            "btn_tooltip" : "Open file",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_save.svg",
            "btn_id" : "btn_save",
            "btn_text" : "Save File",
            "btn_tooltip" : "Save file",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_terminal.png",
            "btn_id" : "btn_terminal",
            "btn_text" : "Open Terminal",
            "btn_tooltip" : "Open Terminal",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_pyinterpreter.png",
            "btn_id" : "btn_pyint",
            "btn_text" : "Open Python CLI",
            "btn_tooltip" : "Open Python CLI",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_settings",
            "btn_text" : "Settings",
            "btn_tooltip" : "Open settings",
            "show_top" : False,
            "is_active" : False
        }
    ]
 
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_emoticons.svg",
            "btn_id" : "btn_about",
            "btn_tooltip" : "About Veritas",
            "is_active" : False
        }
    ]
    
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    def setup_gui(self):
        self.setWindowTitle(self.settings["app_name"])

        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)
     
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to Veritas")
        
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Tab",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        settings = Settings()
        self.settings = settings.items
        
        themes = Themes()
        self.themes = themes.items

        self.toggle = PyToggle(
            width = 50,
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"],
            animation_curve= QEasingCurve.InOutQuad
        )
        self.ui.left_column.menus.btn_1_layout.addWidget(self.toggle, Qt.AlignCenter, Qt.AlignRight)
        self.toggle.stateChanged.connect(lambda: get_state(self.toggle))

        self.ui.load_pages.page_1_layout.addWidget(self.ui.load_pages.label)

        
        self.scrollArea = PyScrollArea()

        self.text_edit = PyTextEdit(
            place_holder_text = "Enter your Python Code Here",
            text = data,
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.scrollArea.setWidget(self.text_edit)
    
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    def py_edit(self, data='', filename='', file_name=None):
        self.scrollArea = PyScrollArea()
        self.scrollArea2 = PyScrollArea()

        self.scrollArea2.setFrameShape(QFrame.NoFrame)
        self.scrollArea2.verticalScrollBar().setStyleSheet("QScrollBar {width:0px;}")

        self.scroll1 = self.scrollArea.verticalScrollBar()

        self.container = QFrame(self.scrollArea)
        self.container2 = QFrame(self.scrollArea2)

        self.layout = QHBoxLayout(self.container)

        self.lay1 = QHBoxLayout(self.container2)
        self.lay2 = QVBoxLayout()
        self.lay3 = QVBoxLayout() 
        self.lay4 = QVBoxLayout() 
        self.lay5 = QHBoxLayout() 
        self.lay6 = QHBoxLayout()
        self.lay7 = QVBoxLayout()

        
        self.bar = PyLabel()

        self.bar.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.sep = PyLabel()
        self.sep.setStyleSheet("""QLabel{
background-color: #4f6d7a;
margin-top: 0px;
max-width: 5px;
}""")

        self.text_edit = PyTextEdit(
            t_btn= self.toggle,
            place_holder_text = "Enter your Python Code Here",
            text = data,
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_one"],
            context_color = self.themes["app_color"]["context_color"]
        )

        self.text_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.completer = PyCompleter()
        self.text_edit.setCompleter(self.completer)

        self.scroll2 = self.text_edit.verticalScrollBar()

        self.memory = PyTextEdit(
            t_btn = self.toggle,
            text = "",
            place_holder_text = "Memory",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_one"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.memory.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.memory.setMaximumHeight(100)
        self.memory.setReadOnly(True)
        self.memory.setCompleter(self.completer)

        self.console = PyTextEdit(
            t_btn = self.toggle,
            place_holder_text = "Console\n\n\n\n\nRun the Program to see the Visualization of the Program",
            text = "",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_one"],
            context_color = self.themes["app_color"]["context_color"]
        )

        self.console.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.console.setReadOnly(True)
        self.console.setCompleter(self.completer)

        self.output = PyTextEdit(
            t_btn = self.toggle,
            
            place_holder_text = "Output",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_one"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.output.setMaximumHeight(80)
        self.output.setReadOnly(True)
        self.output.setCompleter(self.completer)
        
        self.inputs = PyTextEdit(
            t_btn = self.toggle,
            flag_check="input",
            place_holder_text = "Enter all Input Seperated by commas",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_one"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.inputs.setMaximumHeight(80)
        self.inputs.setCompleter(self.completer)

        if file_name == None:
            if filename != "Untitled.py":
                file_name = filename.split('/')
                file_name = file_name.pop()
            else:
                file_name = filename
        
        self.lay1.addWidget(self.bar)
        self.lay1.addWidget(self.text_edit)
        self.lay2.addWidget(self.inputs)
        self.scrollArea2.setWidget(self.container2)
        self.lay3.addWidget(self.scrollArea2)
        self.lay3.addLayout(self.lay2)
        self.lay4.addWidget(self.console)
        self.lay4.addWidget(self.output)
        self.lay5.addLayout(self.lay4)
        self.lay7.addWidget(self.memory)
        self.lay7.addLayout(self.lay5)
        self.layout.addLayout(self.lay3)
        self.layout.addWidget(self.sep)
        self.layout.addLayout(self.lay7)
        self.scrollArea.setWidget(self.container)
            

        self.ui.load_pages.editors.append([self.text_edit, filename, self.bar, self.console, self.memory, self.output, self.inputs])
        self.ui.load_pages.scrolls.append(self.scroll1)
        if file_name != "Untitled.py":
            self.ui.load_pages.tabs.addTab(self.scrollArea, QIcon("gui/images/svg_icons/icon_pyfile.png"), file_name)
        else:
            self.ui.load_pages.tabs.addTab(self.scrollArea, QIcon("gui/images/svg_icons/icon_untitled.png"), file_name)
        
        self.ui.load_pages.tabs.setCurrentWidget(self.scrollArea)
        self.ui.load_pages.page_2_Layout.addWidget(self.ui.load_pages.tabs)
        highlight = synlight.PythonHighlighter(self.text_edit, self.bar, self.ui.load_pages.scrolls, self.ui.load_pages.current_editor, self.ui.load_pages.editors)
        highlight2 = synlight.PythonHighlighter(self.console, self.bar, self.ui.load_pages.scrolls, self.ui.load_pages.current_editor, self.ui.load_pages.editors)
        highlight3 = synlight.PythonHighlighter(self.memory, self.bar, self.ui.load_pages.scrolls, self.ui.load_pages.current_editor, self.ui.load_pages.editors)
        highlight4 = synlight.PythonHighlighter(self.inputs, self.bar, self.ui.load_pages.scrolls, self.ui.load_pages.current_editor, self.ui.load_pages.editors)
        self.text_edit.setFrameStyle((QFrame.NoFrame))

        visualizer(
            self.ui.load_pages.editors,
            self.text_edit,
            self.console,
            self.memory,
            self.output,
            self.inputs,
            save=True
        )

