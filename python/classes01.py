#CLASSES/ESTUDOS/

#Exemplo 01
class Cachorro():
    def __int__(self, cor, raca, altura):
        self.cor = cor
        self.raca = raca
        self.altura = altura

    def Brincar(self, bola):
       if bola == 'azul':
           print('Essa bola não pode!')
       elif bola == 'amarela':
           print('Essa também não pode!')
       else:
           print('Essa pode!')


cachorro = Cachorro()
print(cachorro)

#Exemplo 02:Class para fazer uma compra de tv por assinatura.
class Clientes():
    def __int__(self, nome, email, plano, listar_planos):
        self.nome = nome
        self.email = email
        self.listar_planos = ['basic','top', 'vip']
        if plano in self.listar_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.listar_planos:
            self.plano = novo_plano

        else:
            print('Plano inválido')

cliente = Clientes()




