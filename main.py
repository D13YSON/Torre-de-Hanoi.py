from Torre import Torre
from Disco import Disco
import time

def inicio():
    print('')
    titulo = '### Torre De Hanoi ### '
    print(titulo.center(52))
    print('\n- Mova todos os discos até completar a ultima torre.')
    print('- Discos maiores não podem ficar em cima de discos menores.')
    print('- A quantidade mínima de discos para jogar é 3.')
    print('- A quantidade máxima de discos para jogar é 8.')

    instanciar_disco()
    print_torre()
    torre_origem()


def instanciar_disco():
    qtd_disco = int(input('\nInforme a quantidade de discos: '))

    if qtd_disco >= 3 and qtd_disco <= 8:
        for i in range(1, qtd_disco + 1):
                i = Disco(i)
                t1.empilha(i)
    else:
        print('Min 3, max 8!')
        return instanciar_disco()


def print_torre():
    t1.to_string_torre()
    t2.to_string_torre()
    t3.to_string_torre()


def torre_origem():
    torre = input('\nTorre Origem: ')

    if torre == '1':
        if torre == t1.get_nome():
            if t1.get_tamanho() == 0:
                print('Torre vazia!\n')
                return torre_origem()
            else:
                torre_destino(t1)
                print_torre()
                return torre_origem()

    elif torre == '2':
        if torre == t2.get_nome():
            if t2.get_tamanho() == 0:
                print('Torre vazia!\n')
                return torre_origem()
            else:
                torre_destino(t2)
                print_torre()
                return torre_origem()

    elif torre == '3':
        if torre == t3.get_nome():
            if t3.get_tamanho() == 0:
                print('Torre vazia!\n')
                return torre_origem()
            else:

                torre_destino(t3)
                print_torre()
                return torre_origem()

    else:
        print('Torre inválida!\n')
        return torre_origem()


def torre_destino(self):
    torre = input('Torre Destino: ')
    if t1.get_nome() == torre:
        self.esta_vazia()
        disco = self.desempilha(torre)
        if t1.get_tamanho() == 0:
            t1.movimenta_disco(disco)

        elif disco.get_peso() < t1.torre_discos_peso():
            t1.movimenta_disco(disco)

        else:
            print('Movimento inválido!')
            time.sleep(1)
            return False

    elif t2.get_nome() == torre:
        self.esta_vazia()
        disco = self.desempilha(torre)
        if t2.get_tamanho() == 0:
            t2.movimenta_disco(disco)

        elif disco.get_peso() < t2.torre_discos_peso():
            t2.movimenta_disco(disco)

        else:
            print('Movimento inválido!')
            time.sleep(1)
            return False

    elif t3.get_nome() == torre:
        self.esta_vazia()
        disco = self.desempilha(torre)
        if t3.get_tamanho() == 0:
            t3.movimenta_disco(disco)

        elif disco.get_peso() < t3.torre_discos_peso():
            t3.movimenta_disco(disco)

        else:
            print('Movimento inválido!')
            time.sleep(1)
            return False

    else:
        print('Torre inválida!\n')
        return torre_origem()


if __name__ == '__main__':
    t1 = Torre('1', [])
    t2 = Torre('2', [])
    t3 = Torre('3', [])

inicio()