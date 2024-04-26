from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        
        #labels
        self.header = QLabel("Text Boxes")
        self.setFont(QFont("Helvetica", 24))
        
        
        #text boxes
        self.txtbx = QTextEdit(self,
                               acceptRichText=False,
                               plainText='Welcome',
                               lineWrapMode=QTextEdit.LineWrapMode.FixedColumnWidth,
                               placeholderText='Enter your message here',
                               readOnly=False)
        self.txtbx.setLineWrapMode(self.txtbx.LineWrapMode.FixedColumnWidth)
        self.txtbx.setLineWrapColumnOrWidth(25)
        self.txtbx.setHtml("<font color='red'>Welcome</font>")
        self.txtbx.setFont(QFont("Helvetica", 16))
        
        
        #buttons
        self.button = QPushButton('Submit', clicked=self.click)
        
        
        #showing on the screen
        self.layout().addWidget(self.header)
        self.layout().addWidget(self.txtbx)
        self.layout().addWidget(self.button)
        
        self.show()
        
    def click(self):
        txt = self.txtbx.toPlainText()
        if txt:
            self.label = QLabel(f"You Typed:\n\t\t{txt}")
            self.layout().addWidget(self.label)
        
app = QApplication([])
mw = MainWindow()
app.exec()