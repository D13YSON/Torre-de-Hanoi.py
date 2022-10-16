from Disco import Disco

class Torre:

    def __init__(self,nome,discos):
        self._nome = nome
        self._discos = []

    def get_nome(self):
        return self._nome

    def esta_vazia(self):
        return self._discos == []

    def empilha(self,disco):
        self._discos.append(disco)

    def desempilha(self,nome):
        self.get_nome()
        self._discos.pop(0)


    def get_tamanho(self):
        return len(self._discos)

    def mover_disco(self,torre1,torre2):
        opcao=input('Para qual torre você deseja mover o disco ? ')
        if opcao == 'B':
            self.esta_vazia()
            self.desempilha(opcao)
        ''' self.empilha()'''

    def compara_peso(self,torre):
        for i in self._discos:
             if opcao == torre.get_nome():

                if i.get_peso() > j:
                    print('oi')
                else:
                    print('Fuc')

    def to_string_torre(self):

        print("{:<15} {:<15} ".format('\n'+ self.get_nome(), 'Discos: '+'\n'))

        for i in self._discos:

            print("{:<15} {:<15}".format('',i.get_peso()))

            '''def triangle(n):

                k = n - 1

                for i in range(0, n):

                    for j in range(0, k):
                        print(end=" ")

                    k = k - 1

                    for j in range(0, i + 1):
                        print("□ ", end="")

                    print("\r")
                n = i.get_peso()
                triangle(n)'''
