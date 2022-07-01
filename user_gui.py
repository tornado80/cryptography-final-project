from PySide2.QtWidgets import QApplication, QMainWindow

from user import User
from user_window_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.user = User("Alice")
        self.user_name_line_edit.setText(self.user.name)
        self.user_name_line_edit.textEdited.connect(self.user_name_line_edit_edited)

    def user_name_line_edit_edited(self, new_text):
        self.user.name = new_text


if __name__ == "__main__":
    app = QApplication()
    main_window = MainWindow()
    main_window.show()
    app.exec_()
