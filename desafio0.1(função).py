'''1. Escreva uma função chamada de info que recebe dois parâmetros: nome e telefone e retorne esses parâmetros através do comando return com o f-string dentro da função. Deve criar outra função chamada de menu() e a mesma irá receber os
valores através dos inputs dos usuários.

def info(nome, telefone):
   return f'Seu nome r{nome} e seu telefone é {telefone}'

nome = str(input('digite aqui seu nome: '))
telefone = str(input('digite seu telefone: '))
info (nome, telefone)'''

'''2. Escreva uma função livro que irá receber quatro parâmetros: nome, qtdPaginas, autor e preço. 
Deve retornar essas informações com o comando print dentro da própria função. Em seguida, deve 
criar uma função menu(), o menu irá receber os inputs dos usuários. Mostrem na tela os 
resultados.

def livro(nome, qtdpagina, autor, preco):
   print('Informe seu nome: ', nome)
   print('Informe a de qtdPagina: ', qtdpagina)
   print('Informe o nome do autor: ', autor)
   print('Informe o valor do livro', preco)

def menu():
    nome = str(input('Digite o nome aqui: '))
    qtdpagina = int(input('Qual é a quantidade de páginas: '))
    autor = str(input('Digite o nome do autor: '))
    preco = float(input('Quanto custa o livro: R$'))

    livro(nome, qtdpagina, autor,  preco)

menu()'''

'''3. Faça um programa que receba do usuário o nome do aluno e sua matricula. Retorne essas 
informações na tela. Em seguida, pergunte ao usuário se ele vai querer alterar algum dado de 
seu cadastro, em seguida você deverá realizar essa operação de alteração. Como fará isso? 
Através de funções. A primeira função será alterarNome(nome) e a segunda função será 
alterarMatricula(matricula). Retorne na tela o dado que foi alterado. Dica: Use condicionais.'''

'''def usuario(nome, matricula):
    print('Dados do aluno(a)')
    print(f'Nome: {nome}')
    print(f'Matricula: {matricula}')

nome = str(input(f'Qual é o nome do aluno: '))
matricula = int(input(f'Informe o número da sua matricula: '))

usuario(nome, matricula)

menuopcao = str(input('Você deseja alterar algum dado: 1-sim/2-não'))

if menuopcao.lower() == '1-sim':
    escolha = input('O que você deseja alterar? (nome,matricula)')

    if escolha.lower() == {nome}:
     nome = str(input(f'Qual é o nome do aluno: '))
     print('Alterar:', {nome})

    elif escolha.lower() == {matricula}:
     matricula = int(input(f'Informe o número da sua matricula: '))
     print('Alterar:', {matricula})

else:
    print('Opção inválida')

usuario(nome, matricula)'''


'''ou def alterar(nome):
    novonome = nome
    print('novo nome: ', {novonome})
    
def alterar(matricula):
    novamatricula = matricula 
    print('nova marticula: ', {novamatricula})
    
nome = str(input('')) 
matricula = str(input('')) 
print('')
print('')'''

'''4. Crie um jogo em Python onde o computador vai sortear um número entre 1 até 10. Deve criar uma função para retornar esse número aleatório. Em seguida, crie uma função principal que irá chamar a outra função e 
guardar esse número gerado. Em seguida, você vai tentar adivinhar que número foi esse. A cada tentativa, ele vai te dizer se seu palpite foi alto, baixo ou se você acertou.
· Irá precisar importar a biblioteca, random;
· O número gerado deve estar entre 1 e 10;
· Guarde o número gerado dentro de uma variável;
· Pode utilizar laços de repetição e condicionais.
· Irá utilizar a função randint;'''

'''import random 

def gera():
    return random.randint(1,10) 

def '''


