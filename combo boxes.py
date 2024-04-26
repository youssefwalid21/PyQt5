from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        
        
        #labels
        self.label = QLabel('Where are you from?')
        self.label.setFont(QFont('Helvetica', 24))
        
        
        #combo boxes, dropdown menus
        self.combo = QComboBox(self, editable=True, insertPolicy=QComboBox.InsertPolicy.InsertAtBottom)
        self.regions = ['None','Egypt', 'United States', 'Saudia Arabia']
        self.regions_values = ['None','Egyption', 'American', 'Saudian']
        for i in range(min(len(self.regions), len(self.regions_values))):
            self.combo.addItem(self.regions[i], self.regions_values[i])
            
        
        
        #buttons
        self.button = QPushButton('Show Selection', clicked=self.clicked)
        
        
        #put widgets on the screen
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.combo)
        self.layout().addWidget(self.button)
        
        self.show()
    
    def clicked(self):
        selection = self.combo.currentText()
        self.label.setText(f'You are {selection}')
        
        if selection == 'None':
            self.label.setText('Where are you from?')
            
        
        
        
app = QApplication([])
mw = MainWindow()
app.exec()