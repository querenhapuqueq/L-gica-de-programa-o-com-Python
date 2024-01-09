#Entendendo o self em classes Python
#Classe - Molde(geralmente sem dados)
#Instância da class (objeto) - Tem os dados
#Uma classe pode gerar várias instâncias.
#Na classe o self é a própria instância
class Carro:
    def __int__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerendo...')

fusca = Carro('Fusca')
