from Disco import Disco

class Torre:

    def __init__(self,nome,discos):
        self._nome = nome
        self._discos = []

    def get_nome(self):
        return self._nome

    def esta_vazia(self):
        self._discos == []

    def empilha(self,disco):
        self._discos.append(disco)

    def desempilha(self,nome):
        self.get_nome()
        return  self._discos.pop(0)

    def get_tamanho(self):
        return len(self._discos)

    def torre_discos_peso(self):
        for i in self._discos:
           return i.get_peso()


    def to_string_torre(self):

        print("{:<15} {:<15} ".format('\n'+ self.get_nome(), 'Discos: '+'\n'))

        for i in self._discos:

            print("{:<15} {:<15}".format('',i.get_peso()))

