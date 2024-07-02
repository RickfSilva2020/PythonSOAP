from zeep import Client

# URL do serviço SOAP
url = 'http://127.0.0.1:8000/?wsdl'
client = Client(url)

# Solicitando ao usuário que insira os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicitando ao usuário que escolha a operação
print("Selecione a operação desejada:")
print("1. Adicionar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

escolha = input("Digite sua opção (1/2/3/4): ")

# Realizando a operação escolhida

if escolha == '1':
    print("Resultado: ", client.service.adicionar(num1, num2))
elif escolha == '2':
    print("Resultado: ", client.service.subtrair(num1, num2))
elif escolha == '3':
    print("Resultado: ", client.service.multiplicar(num1, num2))
elif escolha == '4':
    print("Resultado: ", client.service.dividir(num1, num2))
else:
    print("Opção inválida. Tente novamente.")

'''
 Com a Biblioteca colorama
 
from colorama import Fore, Style

if escolha == '1':
    print(Fore.GREEN + "Resultado: ", client.service.adicionar(num1, num2) + Style.RESET_ALL)
elif escolha == '2':
    print(Fore.GREEN + "Resultado: ", client.service.subtrair(num1, num2) + Style.RESET_ALL)
elif escolha == '3':
    print(Fore.GREEN + "Resultado: ", client.service.multiplicar(num1, num2) + Style.RESET_ALL)
elif escolha == '4':
    print(Fore.GREEN + "Resultado: ", client.service.dividir(num1, num2) + Style.RESET_ALL)
else:
    print("Opção inválida. Tente novamente.")
'''
