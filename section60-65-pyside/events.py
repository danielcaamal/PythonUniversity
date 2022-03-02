from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QAction
from PySide6.QtCore import QSize
import sys

class WindowPySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('OOP with PySide')
        self.setFixedSize(400,200)

        # Widget

        # Events
        self.event_button = QPushButton('Click me')
        
        # Signals and Slots
        # Slot
        self.event_button.setCheckable(True)
        # Event Slot
        self.event_button.clicked.connect(self._check)
        # Events
        self.event_button.clicked.connect(self._click_event)
        
        # Connecting the change on title
        self.windowTitleChanged.connect(self._change_title_window)

        # Connecting elements
        self.label = QLabel()
        self.entry_text = QLineEdit()

        # signal(slot)
        self.entry_text.textChanged.connect(self.label.setText)


        # Publishing layout
        layout = QVBoxLayout()
        layout.addWidget(self.entry_text)
        layout.addWidget(self.label)
        layout.addWidget(self.event_button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)


    # Slots and Signals
    def _click_event(self):
        print('Button clicked')
        print('Checked button: ', self.checked_button)

        self.event_button.setText('New Text Button')
        self.event_button.setEnabled(False)
        self.setWindowTitle('New Title')
    
    def _check(self, check):
        self.checked_button = check
        print('Checked?', self.checked_button)

    # Slot change title
    def _change_title_window(self):
        print('Changing title')
        self.setWindowTitle('New Title (Callback)')




if __name__ == '__main__':
    app = QApplication([])
    window = WindowPySide()
    window.show()
    sys.exit(app.exec())