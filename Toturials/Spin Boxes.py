from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.setWindowTitle('Spin Boxes')
        
        #labels
        self.headerLabel = QLabel('Spin Boxes')
        self.headerLabel.setFont(QFont('Arial',24))
        
        
        #spinbox
        self.spin = QSpinBox(self,
                             value=0,
                             maximum=100,
                             minimum=1,
                             singleStep=5,
                             suffix=' years')
        self.spin.setFont(QFont('Arial',20))
        # self.spin
        
        #show
        self.layout().addWidget(self.headerLabel)
        self.layout().addWidget(self.spin)
        
        self.show()
        
app = QApplication([])
mw= MainWindow()
app.exec()