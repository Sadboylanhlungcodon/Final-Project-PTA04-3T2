from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget # them widget tu pyqt6
from PyQt6 import uic # them chuc nang load ui
import sys # them thu vien dieu khien he thong
import webbrowser  

#Lớp trang chủ
class HomeDashBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/Home.ui", self)
        self.btnHome.clicked.connect(self.showHome)
        self.btnHome_2.clicked.connect(self.showHome)
        self.btnProfile.clicked.connect(self.showProfile)
        self.btngold.clicked.connect(self.showGold)
        self.btngold_2.clicked.connect(self.showGold)
        self.btndiamond.clicked.connect(self.showDiamond)
        self.btndiamond_2.clicked.connect(self.showDiamond)
        self.btnruby.clicked.connect(self.showRuby)
        self.btnruby_2.clicked.connect(self.showRuby)
        self.btnsapphire.clicked.connect(self.showSapphire)
        self.btnsapphire_2.clicked.connect(self.showSapphire)
        self.btnemerald.clicked.connect(self.showEmerald)
        self.btnemerald_2.clicked.connect(self.showEmerald)
        self.btnChill.clicked.connect(self.showChill)
        x = None

        #self.btnplaywdta.clicked.connect(lambda _, item=x: self.playMusic(LinkMusic = "https://youtu.be/3AtDnEC4zak?si=I00R3yc3Q7u1x94l"))
        #self.btnplayA.clicked.connect(lambda _, item=x: self.playMusic(LinkMusic = "https://youtu.be/nfs8NYg7yQM?si=3JvQsRQaJXJUZa2I"))
        #self.btnplayoca.clicked.connect(lambda _, item=x: self.playMusic(LinkMusic = "https://youtu.be/BxuY9FET9Y4?si=SPiu6qgm1K8s20UB"))
        #self.btnplayhowlong.clicked.connect(lambda _, item=x: self.playMusic(LinkMusic = "https://youtu.be/CwfoyVa980U?si=OW8eY2QwIGs5GyNS"))
        
        self.btnplaygold.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.pnj.com.vn/site/san-pham/nhan-vang-24k-pnj-0000y001957.html"))
        self.btnplaydiamond.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.pnj.com.vn/site/san-pham/nhan-kim-cuong-vang-trang-18k-pnj-ddddw007786.html"))
        self.btnplayruby.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.pnj.com.vn/site/san-pham/nhan-vang-trang-14k-dinh-da-ruby-pnj-rbddw000195.html"))
        self.btnplaysapphire.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.pnj.com.vn/site/san-pham/nhan-vang-trang-14k-dinh-da-saphire-pnj-spddw000438.html"))
        self.btnplayemerald.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.pnj.com.vn/site/san-pham/nhan-vang-trang-14k-dinh-da-emerald-disneypnj-aladin-erddw000222.html"))
        self.btnplaypickleball.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.youtube.com/watch?v=IzSYlr3VI1A"))
        self.btnplayJ97.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://youtu.be/Lf8df8FCJhk?si=7ToxdFbNImPNa9bB"))
        self.btnplayJ97_2.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://youtu.be/yh5bKLle5lE?si=qFzY9_albRLT6S1n"))
        self.btnplaycomsuonbunmam.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://youtu.be/L4MLcHalj1M?si=t0ReUZlMr63LLbzj"))

    def playMusic(self, LinkShop):
        webbrowser.open(LinkShop)

    

    def showHome(self):
        self.stackedMenu.setCurrentIndex(0)
    def showGold(self):
        self.stackedMenu.setCurrentIndex(1)
    def showDiamond(self):
        self.stackedMenu.setCurrentIndex(2)
    def showRuby(self):
        self.stackedMenu.setCurrentIndex(3)
    def showSapphire(self):
        self.stackedMenu.setCurrentIndex(4)
    def showEmerald(self):
        self.stackedMenu.setCurrentIndex(5)
    def showProfile(self):
        self.stackedMenu.setCurrentIndex(6)
    def showChill(self):
        self.stackedMenu.setCurrentIndex(7)



#Lớp đăng kí
class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI-GiaoDien/signup.ui", self)
        self.btnSignUp.clicked.connect(self.registerAccount)
        self.btnLogin.clicked.connect(self.showLogin)
    def showLogin(self):
        self.close()
        lg.show()
        
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
        self.btnSignUp.clicked.connect(self.showSignUp)
    def showSignUp(self):
        self.close()
        su.show()
    def checkLogin(self):
        username = self.txtEmail.text()
        password = self.txtPassword.text()

        with open("accounts.txt", "r") as file:
            data = file.readlines()
            accounts = []
            for line in data:
                line = line.replace("\n", "")
                line = line.strip()
                accounts.append(line)
        for account in accounts:
            if username == account[0] and password == account[1]:
                self.close()
                home.show()
                return
        if (self.txtEmail.text() + ":" + self.txtPassword.text()) in accounts:
            self.close()
            home.show()

        else:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Lỗi đăng nhập")
            msg_box.setIcon(QMessageBox.Icon.Warning)
            msg_box.setText("Ngu quá trời ơi!\nSai một trong hai\nNhập lại hoặc bye")
            msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
            msg_box.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    lg = Login()
    # Su = SignUp()
    home = HomeDashBoard()
    su = SignUp()
    lg.show()
    sys.exit(app.exec())