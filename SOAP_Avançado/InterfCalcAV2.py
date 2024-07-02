from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from zeep import Client
import sys

class CalculadoraApp(QWidget):
    def __init__(self):
        super().__init__()

        self.client = Client('http://127.0.0.1:8000/?wsdl')

        self.layout = QVBoxLayout()

        self.num1 = QLineEdit(self)
        self.num2 = QLineEdit(self)
        self.result = QLabel('Resultado: ', self)

        self.layout.addWidget(QLabel('Número 1:', self))
        self.layout.addWidget(self.num1)
        self.layout.addWidget(QLabel('Número 2:', self))
        self.layout.addWidget(self.num2)
        self.layout.addWidget(self.result)

        for op in ['Adicionar', 'Subtrair', 'Multiplicar', 'Dividir']:
            btn = QPushButton(op, self)
            btn.clicked.connect(self.calcular)
            self.layout.addWidget(btn)

        self.setLayout(self.layout)

    def calcular(self):
        sender = self.sender()
        num1 = float(self.num1.text())
        num2 = float(self.num2.text())
        operacao = sender.text().lower()

        try:
            resultado = getattr(self.client.service, operacao)(num1, num2)
            self.result.setText('Resultado: ' + str(resultado))
        except Exception as e:
            self.result.setText('Erro: ' + str(e))

app = QApplication(sys.argv)
window = CalculadoraApp()
window.show()
sys.exit(app.exec_())
