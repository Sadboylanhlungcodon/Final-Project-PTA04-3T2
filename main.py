from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QVBoxLayout 
from PyQt6.QtWebEngineWidgets import QWebEngineView # them widget tu pyqt6
from PyQt6.QtCore import QUrl
from PyQt6 import uic # them chuc nang load ui
import sys, json # them thu vien dieu khien he thong
import webbrowser  

class AdminPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI_GiaoDien/Admin.ui", self)
        self.btnAdd.clicked.connect(self.add_row)
        self.btnEdit.clicked.connect(self.edit_row)
        self.btnDelete.clicked.connect(self.delete_row)
        self.btnSave.clicked.connect(self.save_data)
        #self.load_data()

    def load_data(self):
        with open("DATA/test.json", "r") as file:
            data = json.load(file)
            self.tableWidget.setRowCount(0)
            for row in data:
                row_pos = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_pos)
                for col_index, key in enumerate(row):
                    self.tableWidget.setItem(row_pos, col_index, QTableWidgetItem(row[key]))


    def save_data(self):
        with open("DATA/test.json", "w") as file:
            data = []
            for i in range(self.tableWidget.rowCount()):
                ns = self.tableWidget.item(i, 0).text()
                an = self.tableWidget.item(i, 1).text()
                dr = self.tableWidget.item(i, 2).text()
                vi = self.tableWidget.item(i, 3).text()
                Likes = self.tableWidget.item(i, 4).text()
                image = self.tableWidget.item(i, 5).text()
                link = self.tableWidget.item(i, 6).text()
                data.append({"name song": ns, "artist name": an, "duration": dr, "view": vi, "likes": Likes, "image": image, "link": link})
            json.dump(data, file, indent=7)
        # QMessageBox.information(self, "Success", "Data saved successfully!")
                

    def add_row(self):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        self.tableWidget.setItem(row_position, 0, QTableWidgetItem("..."))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem("..."))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem("..."))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem("..."))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem("..."))
        self.tableWidget.setItem(row_position,5, QTableWidgetItem("..."))
        self.tableWidget.setItem(row_position, 6, QTableWidgetItem("..."))
        self.save_data()

    def edit_row(self):
        current_row = self.tableWidget.currentRow()
        current_col = self.tableWidget.currentColumn()
        if current_row < 0:
            QMessageBox.warning(self, "warning", "Please select a row to edit")
            return
        self.tableWidget.setItem(current_row, current_col, QTableWidgetItem("Đã sửa rồi"))
        self.save_data()
    
    def delete_row(self):
        current_row = self.tableWidget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "warning", "Please select a row to delete")
            return
        self.tableWidget.removeRow(current_row)
        self.save_data()

from ui_giaodien.home import Ui_MainWindow

#Lớp trang chủ
class HomeDashBoard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI_GiaoDien/Home.ui", self)
        self.btnHome.clicked.connect(self.showHome)
        self.btnProfile.clicked.connect(self.showProfile)
        self.btnCategory.clicked.connect(self.showCategory)
        self.btnst.clicked.connect(self.showsontung)
        self.btnnnca.clicked.connect(self.shownnca)
        self.btnnnca_2.clicked.connect(self.shownnca)
        self.btnnnca3.clicked.connect(self.shownnca)
        self.btnnnca4.clicked.connect(self.shownnca)
        self.btnnnca5.clicked.connect(self.shownnca)
        self.btnnnca6.clicked.connect(self.shownnca)
        self.btnctktvn.clicked.connect(self.showctktvn)
        self.btnctktvn_2.clicked.connect(self.showctktvn)
        self.btnctktvn3.clicked.connect(self.showctktvn)
        self.btnctktvn4.clicked.connect(self.showctktvn)
        self.btnctktvn5.clicked.connect(self.showctktvn)
        self.btnctktvn6.clicked.connect(self.showctktvn)
        self.btndlttad.clicked.connect(self.showdlttad)
        self.btndlttad_2.clicked.connect(self.showdlttad)
        self.btndlttad3.clicked.connect(self.showdlttad)
        self.btndlttad4.clicked.connect(self.showdlttad)
        self.btndlttad5.clicked.connect(self.showdlttad)
        self.btndlttad6.clicked.connect(self.showdlttad)
        self.btnctctl.clicked.connect(self.showctctl)
        self.btnctctl_2.clicked.connect(self.showctctl)
        self.btnctctl3.clicked.connect(self.showctctl)
        self.btnctctl4.clicked.connect(self.showctctl)
        self.btnctctl5.clicked.connect(self.showctctl)
        self.btnctctl6.clicked.connect(self.showctctl)
        self.btnctcht.clicked.connect(self.showctcht)
        self.btnctcht_2.clicked.connect(self.showctcht)
        self.btnctcht3.clicked.connect(self.showctcht)
        self.btnctcht4.clicked.connect(self.showctcht)
        self.btnctcht5.clicked.connect(self.showctcht)
        self.btnctcht6.clicked.connect(self.showctcht)
        self.btnhth.clicked.connect(self.showHTH)
        self.btnrhyder.clicked.connect(self.showRhyder)
        self.btnatus.clicked.connect(self.showAtus)
        self.btnttpt.clicked.connect(self.showJack)
        self.btnqhmd.clicked.connect(self.showqhmd)
        self.btnrhymastic.clicked.connect(self.showrhymastic)
        self.btnkewtie.clicked.connect(self.showkewtie)
        self.btnkh.clicked.connect(self.showkh)
        self.btntlv.clicked.connect(self.showtlv)
        #self.btnChill.clicked.connect(self.showChill)
        x = None

        #self.btnplaywdta.clicked.connect(lambda _, item=x: self.playMusic(LinkMusic = "https://youtu.be/3AtDnEC4zak?si=I00R3yc3Q7u1x94l"))
        #self.btnplayA.clicked.connect(lambda _, item=x: self.playMusic(LinkMusic = "https://youtu.be/nfs8NYg7yQM?si=3JvQsRQaJXJUZa2I"))
        #self.btnplayoca.clicked.connect(lambda _, item=x: self.playMusic(LinkMusic = "https://youtu.be/BxuY9FET9Y4?si=SPiu6qgm1K8s20UB"))
        #self.btnplayhowlong.clicked.connect(lambda _, item=x: self.playMusic(LinkMusic = "https://youtu.be/CwfoyVa980U?si=OW8eY2QwIGs5GyNS"))
        
        #self.btnplaygold.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.pnj.com.vn/site/san-pham/nhan-vang-24k-pnj-0000y001957.html"))
        #self.btnplaydiamond.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.pnj.com.vn/site/san-pham/nhan-kim-cuong-vang-trang-18k-pnj-ddddw007786.html"))
        #self.btnplayruby.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.pnj.com.vn/site/san-pham/nhan-vang-trang-14k-dinh-da-ruby-pnj-rbddw000195.html"))
        #self.btnplaysapphire.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.pnj.com.vn/site/san-pham/nhan-vang-trang-14k-dinh-da-saphire-pnj-spddw000438.html"))
        #self.btnplayemerald.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.pnj.com.vn/site/san-pham/nhan-vang-trang-14k-dinh-da-emerald-disneypnj-aladin-erddw000222.html"))
        #self.btnplaypickleball.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://www.youtube.com/watch?v=IzSYlr3VI1A"))
        #self.btnplayJ97.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://youtu.be/Lf8df8FCJhk?si=7ToxdFbNImPNa9bB"))
        #self.btnplayJ97_2.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://youtu.be/yh5bKLle5lE?si=qFzY9_albRLT6S1n"))
        #self.btnplaycomsuonbunmam.clicked.connect(lambda _, item=x: self.playMusic(LinkShop = "https://youtu.be/L4MLcHalj1M?si=t0ReUZlMr63LLbzj"))#

    def playMusic(self, LinkShop):
        webbrowser.open(LinkShop)

    

    def showCategory(self):
        self.stackedMenu.setCurrentIndex(0)
    def showsontung(self):
        self.stackedMenu.setCurrentIndex(1)
    def showHTH(self):
        self.stackedMenu.setCurrentIndex(2)
    def showRhyder(self):
        self.stackedMenu.setCurrentIndex(3)
    def showAtus(self):
        self.stackedMenu.setCurrentIndex(4)
    def showJack(self):
        self.stackedMenu.setCurrentIndex(5)
    def showqhmd(self):
        self.stackedMenu.setCurrentIndex(6)
    def showrhymastic(self):
        self.stackedMenu.setCurrentIndex(7)
    def showkewtie(self):
        self.stackedMenu.setCurrentIndex(8)
    def showkh(self):
        self.stackedMenu.setCurrentIndex(9)
    def showtlv(self):
        self.stackedMenu.setCurrentIndex(10)       
    def showProfile(self):
        self.stackedMenu.setCurrentIndex(11)   
    def showctcht(self):
        self.stackedMenu.setCurrentIndex(12)  
    def showctctl(self):
        self.stackedMenu.setCurrentIndex(13)  
    def showdlttad(self):
        self.stackedMenu.setCurrentIndex(14)  
    def showctktvn(self):
        self.stackedMenu.setCurrentIndex(15)  
    def shownnca(self):
        self.stackedMenu.setCurrentIndex(16)  
    def showHome(self):
        self.stackedMenu.setCurrentIndex(17)  

class YouTubeEmbedApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Embed in PyQt6")

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # QWebEngineView to load YouTube

        self.web_view = QWebEngineView
        youtube_url = "https://www.youtube.com/watch?v=kPa7bsKwL-c"  # Replace with your desired YouTube video URL
        self.web_view.setUrl(QUrl(youtube_url))
        
        # Add web view to layout
        layout.addWidget(self.web_view)    


#Lớp đăng kí
class SignUp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI_GiaoDien/signup.ui", self)
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
        uic.loadUi("UI_GiaoDien/login.ui", self)
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
    myapp = QApplication(sys.argv)
    #window = YouTubeEmbedApp()
    #window.resize(800, 600)  # Set window size
    #window.show()
    admin = AdminPage()
    lg = Login()
    Su = SignUp()
    home = HomeDashBoard()
    su = SignUp()
    home.show()
    sys.exit(myapp.exec())

