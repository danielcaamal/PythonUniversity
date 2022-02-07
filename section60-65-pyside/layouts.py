from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, QStackedLayout
from PySide6.QtGui import QAction, QPixmap, QPalette, QColor
from PySide6.QtCore import QSize, Qt
import sys


class Color(QWidget):
    def __init__(self, color):
        '''color - background color'''
        super().__init__()

        # Setting the color
        self.setAutoFillBackground(True)
        palette_colors = self.palette()
        palette_colors.setColor(QPalette.Window, QColor(color))

        # Apply the color
        self.setPalette(palette_colors)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layouts')
        self.setFixedSize(600, 600)
        
        # Vertical Layout
        layoutV = QVBoxLayout()
        layoutV.setContentsMargins(5,5,5,5)
        layoutV.setSpacing(20)
        layoutV.addWidget(Color('red'))
        layoutV.addWidget(Color('green'))
        layoutV.addWidget(Color('blue'))

        # Horizontal Layout
        layoutH = QHBoxLayout()
        layoutH.addWidget(Color('yellow'))
        layoutH.addWidget(Color('purple'))

        # Stack Layout
        layoutS = QStackedLayout()
        layoutS.addWidget(Color('brown'))
        layoutS.addWidget(Color('yellow'))
        layoutS.setCurrentIndex(2)


        # Grid Layout
        layoutG = QGridLayout()
        layoutG.addLayout(layoutV, 0, 0)
        layoutG.addLayout(layoutH, 0, 1)
        # layoutG.addLayout(layoutS, 0, 2)
        layoutG.addWidget(Color('orange'), 1, 0)
        layoutG.addWidget(Color('pink'), 1, 1)

        container = QWidget()
        container.setLayout(layoutG)

        self.setCentralWidget(container)




if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())