import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ZephyrWeb")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.browser.back)

        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.browser.forward)

        self.reload_button = QPushButton("Reload")
        self.reload_button.clicked.connect(self.browser.reload)

        nav_bar = QHBoxLayout()
        nav_bar.addWidget(self.back_button)
        nav_bar.addWidget(self.forward_button)
        nav_bar.addWidget(self.reload_button)
        nav_bar.addWidget(self.url_bar)

        self.layout = QVBoxLayout()
        self.layout.addLayout(nav_bar)
        self.layout.addWidget(self.browser)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
