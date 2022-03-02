from PySide6.QtWidgets import QApplication, QWidget,QPushButton, QMainWindow
import sys

# Event loop
app = QApplication()

# Window object (Any component can be a window)
# window = QWidget()
# window = QPushButton('Push me')
window = QMainWindow()

# Window configuration
window.setWindowTitle('Hello World from PySide')
window.resize(600,400)

# Show the window
window.show()

# Execute application
sys.exit(app.exec())