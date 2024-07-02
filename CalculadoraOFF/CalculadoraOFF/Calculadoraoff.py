# Calculadora simples em Python

def adicionar(x, y):
    return x + y


def subtrair(x, y):
    return x - y


def multiplicar(x, y):
    return x * y


def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y


# Menu de opções
print("Selecione a operação desejada:")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

while True:
    escolha = input("Digite sua opção (1/2/3/4): ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado: ", adicionar(num1, num2))

        elif escolha == '2':
            print("Resultado: ", subtrair(num1, num2))

        elif escolha == '3':
            print("Resultado: ", multiplicar(num1, num2))

        elif escolha == '4':
            print("Resultado: ", dividir(num1, num2))

        # Pergunta ao usuário se ele quer realizar outra operação
        nova_operacao = input("Deseja realizar outra operação? (sim/não): ")
        if nova_operacao.lower() != 'sim':
            break

    else:
        print("Opção inválida. Tente novamente.")
