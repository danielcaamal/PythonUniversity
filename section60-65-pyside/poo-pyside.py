from PySide6.QtWidgets import QApplication,QPushButton, QMainWindow
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize
import sys

class WindowPySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('OOP with PySide')

        # Resizing the window
        # self.resize(600,400)
        self.setFixedSize(QSize(600,400))

        self._add_components()

    def _add_components(self):
        # Adding Menu 
        menu = self.menuBar()

        # Addgin Submenu
        file_menu = menu.addMenu('File')

        # Adding Action
        new_action = QAction('New', self)
        new_action.setStatusTip('New File')

        # Menu + Action
        file_menu.addAction(new_action)

        # Adding Status Bar
        self.statusBar().showMessage('Status Bar Information')

        # Adding Button
        button = QPushButton('New Button')
        self.setCentralWidget(button)


if __name__ == '__main__':
    app = QApplication([])

    window1 = WindowPySide()
    window1.show()
    sys.exit(app.exec())