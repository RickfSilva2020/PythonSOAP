import PySimpleGUI as sg
from suds.client import Client

# URL do serviço SOAP
url = 'http://127.0.0.1:8000/?wsdl'
client = Client(url)

# Layout da interface gráfica
layout = [
    [sg.Text('Número 1'), sg.InputText(key='NUM1')],
    [sg.Text('Número 2'), sg.InputText(key='NUM2')],
    [sg.Text('Resultado', size=(20, 1)), sg.Text('', key='RESULT')],
    [sg.Button('Adicionar'), sg.Button('Subtrair'),
     sg.Button('Multiplicar'), sg.Button('Dividir')]
]

# Janela
window = sg.Window('Calculadora SOAP', layout)

# Event Loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    try:
        num1 = float(values['NUM1'])
        num2 = float(values['NUM2'])
        if event == 'Adicionar':
            result = client.service.adicionar(num1, num2)
        elif event == 'Subtrair':
            result = client.service.subtrair(num1, num2)
        elif event == 'Multiplicar':
            result = client.service.multiplicar(num1, num2)
        elif event == 'Dividir':
            result = client.service.dividir(num1, num2)
        window['RESULT'].update(result)
    except ValueError:
        window['RESULT'].update('Erro: Por favor, insira números válidos.')

window.close()
