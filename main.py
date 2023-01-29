import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout

class Interface(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('Botão')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        self.setCentralWidget(self.cw)
        self.btn.clicked.connect(lambda: print('Lucas lindo'))


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    interface = Interface()
    interface.show()
    qt.exec_()