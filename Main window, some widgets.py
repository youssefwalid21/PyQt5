from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Welcome')
        self.setLayout(QVBoxLayout())

        #Labels
        self.header_label = QLabel('Hello, World!... ENTER YOUR NAME')
        self.fname_label = QLabel('First Name')
        self.lname_label = QLabel('Last Name')
        
        #Inputs
        self.fname_entry = QLineEdit()
        self.lname_entry = QLineEdit()
        
        #Buttons
        self.submit_button = QPushButton(text='Submit',
                                         clicked=self.submit_button_action)
        
        #Show Widgets
        self.layout().addWidget(self.header_label)
        self.layout().addWidget(self.fname_label)
        self.layout().addWidget(self.fname_entry)
        self.layout().addWidget(self.lname_label)
        self.layout().addWidget(self.lname_entry)
        self.layout().addWidget(self.submit_button)
        
        
        self.show()
    
    def submit_button_action(self):
        fname = self.fname_entry.text()
        lname = self.lname_entry.text()
        
        if fname and lname:
            self.header_label.setText(f'Kosom Elsisi\nDo you agree {fname.strip()} {lname.strip()}?')
            
            #yes/kosomo Buttons
            try:
                self.yes_button.setText("Yes of course")
                self.kosomo_button.setText("Kosomo")
            except:
                self.yes_button = QPushButton('Yes of course')
                self.kosomo_button = QPushButton('Kosomo')
            finally:
                #Show the Additional Buttons 
                self.layout().addWidget(self.yes_button)
                self.layout().addWidget(self.kosomo_button)
        else:
            self.header_label.setText('All Fields Are Required')
        
app = QApplication([])
mw = MainWindow()
app.exec()