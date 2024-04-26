from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from os import system

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setLayout(QVBoxLayout())
        self.setWindowTitle("Git Token Maker")
        
        #labels
        self.repo_label = QLabel('Enter the repository link')
        self.token_label = QLabel('Enter the token')
        self.output_label = QLabel("Output")
        
        self.repo_label.setFont(QFont("Helvetica", 24))
        self.token_label.setFont(QFont("Helvetica", 24))
        self.output_label.setFont(QFont("Helvetica", 24))
        
        
        #inputs
        self.repo_entry = QLineEdit()
        self.token_entry = QLineEdit()
        self.output_entry = QLineEdit()
        
        self.repo_entry.setPlaceholderText("Ex:- https://github.com/username/reponame.git")
        self.token_entry.setPlaceholderText("Get it from your Github")
        
        self.repo_entry.setFont(QFont("Helvetica", 18))
        self.token_entry.setFont(QFont("Helvetica", 18))
        self.output_entry.setFont(QFont("Helvetica", 18))
        
        self.output_entry.setEnabled(False)
        
        
        #buttons
        self.create_button = QPushButton('Create Full Token', clicked=self.createToken)
        self.create_button.setFont(QFont("Helvetica", 18))

        
        #show on the screen
        self.layout().addWidget(self.repo_label)
        self.layout().addWidget(self.repo_entry)
        self.layout().addWidget(self.token_label)
        self.layout().addWidget(self.token_entry)
        self.layout().addWidget(self.output_label)
        self.layout().addWidget(self.output_entry)
        self.layout().addWidget(self.create_button)
        
        
        self.show()
    
    def createToken(self):
        repo = self.repo_entry.text()
        token = self.token_entry.text()
        if not token and not repo:
            return
        index = repo.rfind('github.com')
        
        full = ''
        
        for i, char in enumerate(repo, 0):
            full += char
            if i == index - 1:
                full += token + '@'
        repo_name = repo[repo.rfind('/') + 1:repo.rfind('.')]
        try:
            file = open(f'Tokens\\{repo_name}.txt', 'w')
        except FileNotFoundError:
            system('mkdir Tokens')
            file = open(f'Tokens\\{repo_name}.txt', 'w')
        finally:
            file.write(f'Repo Link: {repo}\nGithub Token: {token}\nRepo Name: {repo_name}\nGit Token: {full}\n')
        self.output_entry.setEnabled(True)
        self.output_entry.setText(full)
        
        
app = QApplication([])
mw = MainWindow()
app.exec()
