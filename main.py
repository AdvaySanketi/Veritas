#import pyi_splash
from gui.core.flowchart import flowchart
from gui.core.internet_check import internet_connectivity_check
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os

from qt_core import *

from gui.core.json_settings import Settings
from gui.core.terminal import pyint, terminal, run_file
from gui.uis.windows.main_window import *

from gui.widgets import *

from threading import *

from gui.core.visualize import check_input, visualize, setting_up, display_error
from gui.core.pyparts import dismantle

os.environ["QT_FONT_DPI"] = "96"

count = 0
count2 = 0
cnt = 0
data = ''
filename = ''
editor = None

def file_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except:
        pass

class MainWindow(QMainWindow):
    def __init__(self):
        global internet
        super(MainWindow, self).__init__()
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        settings = Settings()
        self.settings = settings.items
        self.hide_grips = True
        SetupMainWindow.setup_gui(self)
        self.show()
        editor = MainFunctions.get_left_menu_btn(self, "btn_editor")
        editor.setVisible(False)
        #pyi_splash.close()
        with open("gui//core//vislist.txt",'w'):
            pass
    
    def btn_clicked(self):
        btn = SetupMainWindow.setup_btns(self)
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        if btn.objectName() == "btn_home":
            global count
            self.ui.left_menu.select_only_one(btn.objectName())
            if count == 0:
                MainFunctions.set_page(self, self.ui.load_pages.page_1)
            else:
                MainFunctions.set_page(self, self.ui.load_pages.page_2)
        
        if btn.objectName() == "btn_editor":
            self.ui.left_menu.select_only_one(btn.objectName())
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
        
        if btn.objectName() == "btn_new_file":
            global data
            global editor
            data = ''
            SetupMainWindow.py_edit(self, data, "Untitled.py")
            Home = MainFunctions.get_left_menu_btn(self, "btn_home")
            Home.setVisible(False)
            editor = MainFunctions.get_left_menu_btn(self, "btn_editor")
            editor.setVisible(True)
            self.ui.left_menu.select_only_one('btn_editor')
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
            count += 1

        if btn.objectName() == "btn_run":
            self.ui.left_menu.select_only_one('btn_home')
            if not check_input(self.ui.load_pages.current_editor.toPlainText()):
                dismantle(self.ui.load_pages.current_editor.toPlainText())
                err = run_file("gui//core//breakdown.py")
                if err != None:
                    display_error(err)
                setting_up()
                visualize(_code = self.ui.load_pages.current_editor.toPlainText(),tabindex=self.ui.load_pages.tabs.currentIndex())
            else:
                dismantle(self.ui.load_pages.current_editor.toPlainText())
                setting_up()
                visualize(_code = self.ui.load_pages.current_editor.toPlainText(),tabindex=self.ui.load_pages.tabs.currentIndex())
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        if btn.objectName() == "btn_flowchart":
            if internet_connectivity_check():
                flowchart(self.ui.load_pages.current_editor.toPlainText())
                MainFunctions.set_page(self, self.ui.load_pages.page_2)
            else:
                msgBox = QMessageBox()
                msgBox.setText("You are Currenty Offline")
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Veritas No Internet")
                msgBox.setInformativeText("Please turn on Wifi and Then Try again")
                msgBox.exec()
        
        if btn.objectName() == "btn_terminal":
            terminal()

        if btn.objectName() == "btn_pyint":
            pyint()

        if btn.objectName() == "btn_open_file":
            filename, _ = QFileDialog.getOpenFileName(self, "Open File",None, "Python Files (*.py)")
            data = file_data(filename)
            if data != None:
                if filename.endswith(".py"):
                    count += 1
                    SetupMainWindow.py_edit(self, data, filename)
                    Home = MainFunctions.get_left_menu_btn(self, "btn_home")
                    Home.setVisible(False)
                    editor = MainFunctions.get_left_menu_btn(self, "btn_editor")
                    editor.setVisible(True)
                    self.ui.left_menu.select_only_one('btn_editor')
                    MainFunctions.set_page(self, self.ui.load_pages.page_2)

        if btn.objectName() == "btn_save":
            if count != 0 or cnt != 0:
                page = str(MainFunctions.get_page(self)).split(' ')[1].replace('name="','').replace('")', '')
                if page == "page_2":
                    contents = SetupMainWindow.extract_text(self, "py")
                    for i in self.ui.load_pages.editors:
                        if i[0] == self.ui.load_pages.current_editor:
                            if not i[1] == "Untitled.py":
                                file_loc = i[1]
                            else:
                                name = QFileDialog.getSaveFileName(self, 'Save File', None, "All Files (*);; Python files (*.py)")
                                filename = name[0]
                                file_loc = name[0]
                    with open(file_loc, 'w') as file:
                        file.write(contents)
                    file.close()
                    for i in self.ui.load_pages.editors:
                        if i[0] == self.ui.load_pages.current_editor:
                            if i[1] == "Untitled.py":
                                self.ui.load_pages.editors.remove(i)
                                self.ui.load_pages.editors.insert(self.ui.load_pages.tabs.currentIndex() , [i[0], file_loc])
                                self.ui.load_pages.tabs.setTabText(self.ui.load_pages.tabs.currentIndex(), file_loc.split('/')[-1])
                                self.ui.load_pages.tabs.setTabIcon(self.ui.load_pages.tabs.currentIndex(), QIcon("gui/images/svg_icons/icon_pyfile.png"))
                    self.ui.left_menu.select_only_one('btn_home')
                    MainFunctions.set_page(self, self.ui.load_pages.page_2)
                else:
                    pass

        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            if not MainFunctions.left_column_is_visible(self):
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
                
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self, 
                    menu = self.ui.left_column.menus.menu_1,
                    title = "Settings Tab",
                    icon_path = Functions.set_svg_icon("icon_settings.svg")
                )

        if btn.objectName() == "btn_about":
            MainFunctions.set_right_column_menu(
                    self,
                    self.ui.right_column.menu_1)

            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)
                MainFunctions.toggle_right_search(self)
            else:
                btn.set_active(False)
                MainFunctions.toggle_right_search(self)
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)

    
    def btn_released(self):
        btn = SetupMainWindow.setup_btns(self)

    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())