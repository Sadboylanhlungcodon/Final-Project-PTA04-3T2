from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget # them widget tu pyqt6
from PyQt6 import uic # them chuc nang load ui
import sys # them thu vien dieu khien he thong

#Lớp đăng kí
class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/signup.ui", self)
        self.btnSignUp.clicked.connect(self.registerAccount)
        
    def registerAccount(self):
        username = self.txtEmail
        password = self.txtPassword
        confirmPassword = self.txtconfirmPassword
        if username.text() == "":
            username.setFocus()
            return
        if password.text() == "":
            password.setFocus()
            return
        if confirmPassword.text() == "":
            confirmPassword.setFocus()
            return
        if username.text().find("gmail.com") == -1:
            username.clear()
            username.setFocus()
            return
        with password.text() != confirmPassword.text():
            confirmPassword.setFocus()
            return
        with open("accounts.txt", "a") as file:
            file.write(username.text() + " " + password.text() + "\n")
        self.close()

class Login(QMainWindow):
    # ham khoi tao giao dien UI
    def __init__(self):
        super().__init__()
        # doc giao dien tu file login.ui
        uic.loadUi("Ui-GiaoDien/login.ui", self)
        self.btnLogin.clicked.connect(self.checkLogin)
    def checkLogin(self):
        with open("accounts.txt", "r") as file:
            data = file.readlines()
            accounts = []
            for line in data:
                line = line.replace("\n", "")
                line = line.strip()
                accounts.append(line)
        if (self.txtEmail.text() + ":" + self.txtPassword.text()) in accounts:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lg = Login()
    Su = SignUp()
    Su.show()
    app.exec()