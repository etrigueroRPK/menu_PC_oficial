import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLineEdit
from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

import os
class Widgets(QMainWindow):
 
    def __init__(self):
        QMainWindow.__init__(self)
       
        self.widget = QWidget(self)
 
        # Widget para el navegador
        self.webview = QWebEngineView()
        # self.webview.scroll()
        # self.webview.load(QUrl("https://www.google.com/"))
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "dev_pollos_copacabana/index.html"))
        print(file_path)
        self.webview.load(QUrl.fromLocalFile(file_path))


        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.webview)
 
        self.widget.setLayout(self.layout)
        
        # self.setWindowFlags ( Qt.FramelessWindowHint)
        self.setCentralWidget(self.widget)
       
    
    
 
if __name__ == "__main__":
    # print(file_path)
    app = QApplication(sys.argv)
    window = Widgets()
    
    
    window.showFullScreen()
    
    sys.exit(app.exec_())