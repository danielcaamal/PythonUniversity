from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QToolBar, QStatusBar
from PySide6.QtGui import QAction, QPixmap, QPalette, QColor, QIcon
from PySide6.QtCore import QSize, Qt
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Toolbars')
        self.setFixedSize(600, 600)
        label = QLabel('Hello')
        label.setAlignment(Qt.AlignCenter)

        # ToolBar
        toolbar = QToolBar('My Toolbar')
        toolbar.setIconSize(QSize(16,16))
        # toolbar.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.addToolBar(toolbar)

        # Actions
        new_button = QAction(QIcon('section60-65-pyside/nuevo.png'), 'New', self)
        new_button.setStatusTip('New File')
        # new_button.setCheckable(True)
        toolbar.addAction(new_button)

        # Icons

        # Event
        new_button.triggered.connect(self._click_new_button)

        self.setStatusBar(QStatusBar(self))

        # Menus
        menu = self.menuBar()
        file_submenu = menu.addMenu('&File')
        file_submenu.addAction(new_button)
    
    def _click_new_button(self, click):
        print(f'Click event: {click}')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())