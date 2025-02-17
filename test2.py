from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys


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
        self.web_view = QWebEngineView()
        youtube_url = "https://www.youtube.com/watch?v=kPa7bsKwL-c"  # Replace with your desired YouTube video URL
        self.web_view.setUrl(QUrl(youtube_url))
        
        # Add web view to layout
        layout.addWidget(self.web_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeEmbedApp()
    window.resize(800, 600)  # Set window size
    window.show()
    sys.exit(app.exec())