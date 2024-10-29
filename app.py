import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon  # Import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("widgetbrowserbymarmik")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("favicon.ico"))  # Set your icon here

        # Create a QWebEngineView widget
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))  # Start with a default page
        self.setCentralWidget(self.browser)

        # Create a toolbar for navigation
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        # Back action
        back_action = QAction('Back', self)
        back_action.triggered.connect(self.browser.back)
        self.toolbar.addAction(back_action)

        # Forward action
        forward_action = QAction('Forward', self)
        forward_action.triggered.connect(self.browser.forward)
        self.toolbar.addAction(forward_action)

        # Reload action
        reload_action = QAction('Reload', self)
        reload_action.triggered.connect(self.browser.reload)
        self.toolbar.addAction(reload_action)

        # Close action
        close_action = QAction('Close', self)
        close_action.triggered.connect(self.close)
        self.toolbar.addAction(close_action)

        # Optionally add minimize and maximize actions
        minimize_action = QAction('Minimize', self)
        minimize_action.triggered.connect(self.showMinimized)
        self.toolbar.addAction(minimize_action)

        maximize_action = QAction('Maximize', self)
        maximize_action.triggered.connect(self.showMaximized)
        self.toolbar.addAction(maximize_action)

        # Set window flags to allow resizing and moving
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
