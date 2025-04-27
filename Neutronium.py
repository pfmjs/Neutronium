import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QIcon

class Neutronium(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Neutronium")
        self.setWindowIcon(QIcon("icon.ico"))
        self.browser = QWebEngineView()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "src", "index.html")

        if os.path.exists(path):
            self.browser.load(QUrl.fromLocalFile(path))
            self.setCentralWidget(self.browser)
            self.browser.page().runJavaScript("document.body.style.overflow = 'scroll';")
        else:
            self.show_tutorial_page()

        self.show()

    def keyPressEvent(self, event):
        if event.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier) and event.key() == Qt.Key_I:
            self.browser.page().triggerAction(self.browser.page().InspectElement)
        elif event.key() == Qt.Key_F5:
            self.browser.reload()
        else:
            super().keyPressEvent(event)

    def show_tutorial_page(self):
        widget = QWidget()
        layout = QVBoxLayout()
        tutorial_label = QLabel(
            "Tutorial\nCreate a src folder with index.html\n\nTip: Press F5 to reload the page"
        )
        tutorial_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(tutorial_label)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = Neutronium()
sys.exit(app.exec_())