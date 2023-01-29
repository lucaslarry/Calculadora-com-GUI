import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
   
   
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora Lucas') #Mudar o Nome da Aba 
        self.setFixedSize(300, 400) #Definir um tamanho fixo pra aba
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.display = QLineEdit() #O input
        self.grid.addWidget(self.display, 0, 0, 1, 4)
        self.display.setDisabled(True) #Para o usuario não conseguir digitar no input
        self.display.setText('')
        self.display.setStyleSheet(
            '* {background: #000000; color: #DCDCDC; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        self.adicionar_botao(QPushButton('7'), 2, 0, 1, 1,'background: #696969; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton('8'), 2, 1, 1, 1,'background: #696969; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton('9'), 2, 2, 1, 1,'background: #696969; color: #FFF; font-weight: 100')
        
        self.adicionar_botao(QPushButton('4'), 3, 0, 1, 1,'background: #696969; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton('5'), 3, 1, 1, 1,'background: #696969; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton('6'), 3, 2, 1, 1,'background: #696969; color: #FFF; font-weight: 100')
        
        self.adicionar_botao(QPushButton('1'), 4, 0, 1, 1,'background: #696969; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton('2'), 4, 1, 1, 1,'background: #696969; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton('3'), 4, 2, 1, 1,'background: #696969; color: #FFF; font-weight: 100')
        
        self.adicionar_botao(QPushButton('.'), 5, 0, 1, 1,'background: #808080; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton('0'), 5, 1, 1, 1,'background: #696969; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton(''), 5, 2, 1, 1,'background: #808080; color: #FFF; font-weight: 100')
        
        self.adicionar_botao(
            QPushButton('C'), 
            1, 0, 1, 1,
            'background: #696969; color: #FFF; font-weight: 100',
            lambda: self.display.setText('')
        )
        self.adicionar_botao(QPushButton(''), 1, 1, 1, 1,'background:#808080; color: #FFF; font-weight: 100')
        self.adicionar_botao(
            QPushButton('⌫'),
             1, 2, 1, 1,
             'background: #696969; color: #FFF; font-weight: 100',
             lambda: self.display.setText(
                self.display.text()[:-1]
             )
             )
        self.adicionar_botao(QPushButton('/'), 1, 3, 1, 1,'background: #FF8C00; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton('*'), 2, 3, 1, 1,'background: #FF8C00; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton('+'), 3, 3, 1, 1,'background: #FF8C00; color: #FFF; font-weight: 100')
        self.adicionar_botao(QPushButton('-'), 4, 3, 1, 1,'background: #FF8C00; color: #FFF; font-weight: 100')
        self.adicionar_botao(
            QPushButton('='), 
            5, 3, 1, 1,
            'background: #B22222; color: #FFF; font-weight: 100',
            lambda: self.resultado()
            )


        self.setCentralWidget(self.cw)


    def adicionar_botao(self, botao, row, col, rowspan, colspan, style = None, funcao = None ):
        self.grid.addWidget(botao, row, col, rowspan, colspan)
        
        if not funcao:
            botao.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + botao.text()
                )
            )
        
        else:
            botao.clicked.connect(funcao)
        
        botao.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        if style:
            botao.setStyleSheet(style)
    

    def resultado(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta inválida')


        


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calculadora = Calculadora()
    calculadora.show()
    qt.exec_()
    