import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QPlainTextEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(320, 0)
        btn.show()

        textbox = QPlainTextEdit()
        textbox.resize(100, 100)
        textbox.move(320, 100)
        # self.layout.addWidget(self.textbox)
        textbox.show()

        self.setGeometry(363, 204, 640, 360)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
