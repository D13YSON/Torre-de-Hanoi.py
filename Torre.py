from Disco import Disco

class Torre:
    def __init__(self,nome,discos):
        self._nome = nome
        self._discos = []


    def get_nome(self):
        return self._nome


    def get_tamanho(self):
        return len(self._discos)


    def esta_vazia(self):
        self._discos == []


    def torre_discos_peso(self):
        for i in self._discos:
           return i.get_peso()


    def empilha(self,disco):
        self._discos.append(disco)


    def desempilha(self,nome):
        self.get_nome()
        return  self._discos.pop(0)



    def movimenta_disco(self,disco):
        self._discos.insert(0, disco)


    def to_string_torre(self):
        print("{:<15} {:<15} ".format('\n'+ self.get_nome(), 'Discos: '+'\n'))

        for i in self._discos:
            print("{:<15} {:<15}".format('',i.get_peso()))



        '''print("{:<15}  {:<15}".format('\n'+ self.get_nome(), 'Discos: '+'\n'))

        for i in self._discos:

            print("{:<15} {:<15} ".format('',i.get_peso()))

            def triangle(n):

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



