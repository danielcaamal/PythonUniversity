from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QVBoxLayout, QWidget, QCheckBox, QHBoxLayout, QListWidget, QLineEdit, QSpinBox, QDoubleSpinBox, QSlider, QDial
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtCore import QSize, Qt
import sys

class Components(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Components')
        self.setFixedSize(500, 600)
        
        # Label Widget
        self.subtitle1 = QLabel('Labels:')
        self.label = QLabel('Hello World')

        # Change the label's attrs
        # Text
        self.label.setText('Greetings')
        # Font
        font = self.label.font()
        font.setPointSize(25)
        self.label.setFont(font)
        # Alignment
        self.label.setAlignment(Qt.AlignCenter) # =  Qt.AlignHCenter | Qt.AlignVCenter

        # Image Widget
        self.subtitle2 = QLabel('Image:')
        self.image = QLabel('Image')
        self.image.setPixmap(QPixmap('./section60-65-pyside/layla.jpg'))
        self.image.setScaledContents(True)

        # CheckBox Widget
        self.subtitle3 = QLabel('CheckBox:')
        self.checkbox = QCheckBox('This is a CheckBox')
        self.checkbox.setTristate(True)
        self.checkbox.stateChanged.connect(self._show_state)

        # ComboBox Widget
        self.subtitle4 = QLabel('ComboBox:')
        self.combobox = QComboBox()
        self.combobox.addItem('One')
        self.combobox.addItems(['Two', 'Three'])
        self.combobox.currentIndexChanged.connect(self._change_index)
        self.combobox.currentTextChanged.connect(self._change_text)
        self.combobox.setEditable(True)
        self.combobox.setMaxCount(6)
        # Policies:
        # QComboBox.NoInsert + Enter => Do nothing
        # QComboBox.InsertAtTop + Enter => Insert new item at Top
        # QComboBox.InsertAtCurrent + Enter => Update current item
        # QComboBox.InsertAtBottom + Enter => Insert new item at Bottom
        self.combobox.setInsertPolicy(QComboBox.InsertAtBottom)

        # QList Widget
        self.subtitle5 = QLabel('ListWidget:')
        self.list_widget = QListWidget()
        self.list_widget.addItems(['One', 'Two', 'Three'])
        self.list_widget.currentItemChanged.connect(self._change_element)

        # QLine Edit
        self.subtitle6 = QLabel('Line Edit:')
        self.line_edit = QLineEdit()
        self.line_edit.setMaxLength(16)
        self.line_edit.setPlaceholderText('Placeholder')
        # self.line_edit.setReadOnly(True)
        self.line_edit.setInputMask('000-0000-0000')
        self.line_edit.returnPressed.connect(self._enter_pressed)
        self.line_edit.selectionChanged.connect(self._change_selection)
        self.line_edit.textChanged.connect(self._change_text_le)

        # SpinBox
        self.subtitle7 = QLabel('SpinBox:')
        self.spin_box = QDoubleSpinBox()
        self.spin_box.setMaximum(10)
        self.spin_box.setMinimum(0)
        self.spin_box.setRange(0, 10)
        self.spin_box.setPrefix('$')
        self.spin_box.setSuffix('c')
        self.spin_box.setSingleStep(2)
        self.spin_box.valueChanged.connect(self._change_value)
        self.spin_box.textChanged.connect(self._change_text_sb)

        # Slider
        self.subtitle8 = QLabel('Slider:')
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(-5,15)
        self.slider.valueChanged.connect(self._change_value_s)
        self.slider.sliderMoved.connect(self._change_slider)

        # Dial
        self.subtitle9 = QLabel('Dial:')
        self.dial = QDial()
        self.dial.setRange(-5,15)


        # Publishing layout
        layoutV1 = QVBoxLayout()
        layoutV2 = QVBoxLayout()

        # Column 1
        layoutV1.addWidget(self.subtitle1)
        layoutV1.addWidget(self.label)
        layoutV1.addWidget(self.subtitle2)
        layoutV1.addWidget(self.image)

        # Column 2
        layoutV2.addWidget(self.subtitle3)
        layoutV2.addWidget(self.checkbox)
        layoutV2.addWidget(self.subtitle4)
        layoutV2.addWidget(self.combobox)
        layoutV2.addWidget(self.subtitle5)
        layoutV2.addWidget(self.list_widget)
        layoutV2.addWidget(self.subtitle6)
        layoutV2.addWidget(self.line_edit)
        layoutV2.addWidget(self.subtitle7)
        layoutV2.addWidget(self.spin_box)
        layoutV2.addWidget(self.subtitle8)
        layoutV2.addWidget(self.slider)
        layoutV2.addWidget(self.subtitle9)
        layoutV2.addWidget(self.dial)

        layoutH1 = QHBoxLayout()
        layoutH1.addLayout(layoutV1)
        layoutH1.addLayout(layoutV2)

        container = QWidget()
        container.setLayout(layoutH1)

        self.setCentralWidget(container)

    # Checkbox
    def _show_state(self, state):
        print('CheckBox State:', state)
        # Working with constants
        if state == Qt.Checked:                     # 2
            print('CheckBox checked')
        elif state == Qt.PartiallyChecked:          # 1
            print('CheckBox partially checked')
        else:                                       # 0
            print('CheckBox not checked')
    
    # ComboBox
    def _change_index(self, index):
        print('ComboBox new index:', index)
    
    def _change_text(self, text):
        print('ComboBox new text:', text)

    # List Widget
    def _change_element(self, element):
        print('List Widget new element:', element.text())

    # Line Edit
    def _enter_pressed(self):
        print('Enter pressed')
        self.line_edit.setText('Enter Pressed')
    
    def _change_selection(self):
        print('Change text selected')
        print(self.line_edit.selectedText())

    def _change_text_le(self, text):
        print('Change text:', text)

    # SpinBox
    def _change_value(self, value):
        print('Change value:', value)
    
    def _change_text_sb(self, value):
        print('Change value:', value)

    # Slider
    def _change_value_s(self, value):
        print('Change value:', value)
    
    def _change_slider(self, value):
        print('Change slider:', value)
    







if __name__ == '__main__':
    app = QApplication([])
    window = Components()
    window.show()
    sys.exit(app.exec())
