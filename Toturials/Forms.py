from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.setLayout(QVBoxLayout)
        self.formLayout = QFormLayout()
        self.setLayout(self.formLayout)
        self.setFont(QFont("Helvetica", 14))
        
        
        #labels
        self.header_label = QLabel("Hey You!...Enter your name")
        self.header_label.setFont(QFont("Helvetica", 30))
        
        
        #inputs
        self.fname_entry = QLineEdit(self)
        self.lname_entry = QLineEdit(self)
        
        
        #button
        self.button = QPushButton("Submit", clicked=self.click)
        # self.setFont(QFont("Helvetica", 14))
        
        
        #forms
        self.formLayout.addRow(self.header_label)
        self.formLayout.addRow('First name', self.fname_entry)
        self.formLayout.addRow('Last name', self.lname_entry)
        self.formLayout.addRow(self.button)
        
        self.show()
        
    def click(self):
        fname = self.fname_entry.text()
        lname = self.lname_entry.text()
        
        if fname and lname:
            self.header_label.setText(f'Welcome {fname} {lname}')
            
            self.fname_entry.setText('')
            self.lname_entry.setText('')
        
app = QApplication([])
mw = MainWindow()
app.exec()