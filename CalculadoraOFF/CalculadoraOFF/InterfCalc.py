import PySimpleGUI as sg

# Funções da calculadora
def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    return "Erro" if y == 0 else x / y

# Layout da interface gráfica
layout = [
    [sg.Text('Número 1'), sg.InputText(key='NUM1')],
    [sg.Text('Número 2'), sg.InputText(key='NUM2')],
    [sg.Text('Resultado', size=(20,1)), sg.Text('', key='RESULT')],
    [sg.Button('Adicionar'), sg.Button('Subtrair'), sg.Button('Multiplicar'), sg.Button('Dividir')]
]

# Janela
window = sg.Window('Calculadora', layout)

# Event Loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    try:
        num1 = float(values['NUM1'])
        num2 = float(values['NUM2'])
        if event == 'Adicionar':
            result = adicionar(num1, num2)
        elif event == 'Subtrair':
            result = subtrair(num1, num2)
        elif event == 'Multiplicar':
            result = multiplicar(num1, num2)
        elif event == 'Dividir':
            result = dividir(num1, num2)
        window['RESULT'].update(result)
    except ValueError:
        window['RESULT'].update('Erro: Por favor, insira números válidos.')


window.close()
