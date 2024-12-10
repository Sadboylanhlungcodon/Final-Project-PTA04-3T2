import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic 

class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/test.ui", self)

        self.pushButton.clicked.connect(self.show_note_page)
        self.btnHome.clicked.connect(self.showHome)
    
    def showHome(self):
        self.stackedWidget.setCurrentIndex(0)  
    def show_note_page(self):
        self.stackedWidget.setCurrentIndex(1)  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    NT = NoteApp()
    NT.show()
    app.exec()