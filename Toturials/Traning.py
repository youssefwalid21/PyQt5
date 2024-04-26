from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setLayout(QVBoxLayout())
        
        #label
        self.header = QLabel('Welcome... What\'s your name?')
        self.header.setFont(QFont('Helvetica', 24))
        
        #inputs
        self.entry = QLineEdit()
        self.entry.setFont(QFont("Helvetica", 16))
        self.entry.setPlaceholderText('Full name')
        
        #buttons
        self.prev = QPushButton('Previous', clicked=self.prevaction)
        self.prev.setEnabled(False)
        self.prev.setFont(QFont('Helvetica', 16))
        
        self.next = QPushButton('Next', clicked=self.nextaction)
        self.next.setFont(QFont('Helvetica', 16))
        
        
        
        #show
        self.layout().addWidget(self.header)
        self.layout().addWidget(self.entry)
        self.layout().addWidget(self.next)
        self.layout().addWidget(self.prev)
        
        self.show()
    def nextaction(self):
        self.header.setText(f"Welcome {self.entry.text().strip()}, Enter your age")
        self.entry.setText('')
        self.entry.setPlaceholderText('Age')
        self.prev.setEnabled(True)
        self.next.setText('Confirm')

    def prevaction(self):
        self.prev.setEnabled(False)
        self.header.setText('Welcome... What\'s your name?')
        self.entry.setPlaceholderText('Full name')
        self.entry.setText('')
        self.next.setText('Next')
    
    

app = QApplication([])
mw = MainWindow()
app.exec()