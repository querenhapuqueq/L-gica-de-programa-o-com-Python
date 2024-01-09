#desvios condicionais

# simples

"""condicao = int(input("Digite aqui o valor: "))

if condicao == 10:
    print("o valor é 10!")

if condicao == 2:
    print("Mostra a instrução")

if condicao == 9:
    print("Mostra a instrução")"""

# composta

"""condicao = int(input("Digite aqui o valor: "))

if condicao == 2:
    print("Mostra a instrução!")
else:
    print("Mostra outra instrução")

print("Será mostrado")"""

#condicional encadeada

'''Exemplo 1'''

"""valor1 = int(input("Digite aqui o valor 1: "))
valor2 = int(input("Digite aqui o valor 2: "))

if valor1 < valor2:
    print("X é menor que y!")
elif valor1 > valor2:
    print("X é maior que y!")
else:
    print("Os dois são iguais")"""

'''Exemplo 2'''

"""entrada = input("Você deseja entrar ou sair: ")

if entrada == 'entrar':
    print("Você entrou no sistema")
elif entrada == 'sair':
    print("Você saiu do sistema")
else:
    print("Você digitou errado!")"""

#condicionais aninhadas

"""valor1 = int(input("Digite aqui o valor 1: "))
valor2 = int(input("Digite aqui o valor 2: "))

if valor1 == valor2:
    print("valores são iguias!")
else:
    if valor1 < valor2:
     print("Valor1 é menor")
    else:
        print("Valor1 é maior")"""

valor1 = 12
valor2 = 5

if valor1 == valor2:
    print("valores são iguias!")
else:
    if valor1 < valor2:
     print("Valor1 é menor")
    else:
        print("Valor1 é maior")

