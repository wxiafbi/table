import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# 用QMainWindow的子类来自定义你应用的窗口
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # 必须有，继承父类的构造方法

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # 设置窗口的中心部件
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
