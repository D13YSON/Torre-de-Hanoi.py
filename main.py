from Torre import Torre
from Disco import Disco

def menu():
    print('\n--- Torre de Hanoi ----')
    print('1 - Start')
    print('2 - Exit')
    print('-----------------------\n')

    opacao=int(input('Digite uma das opções acima: '))

    if opacao== 1 :
       star()

    elif opacao== 2:

        resposta=input('Deseja realmente sair do jogo? Sim ou Não ! ')

        if 'Sim' == resposta:
            exit()

        else:

            return menu()

    else:
        print('\nOpção invalida!Digite apenas 1 ou 2')
        return menu()

def star():
    instanciar_d()
    print_torre()
    perguntar_t()

def instanciar_d():
    print('Com quantos discos você que jogar? (OBS: no mínimo 3 discos ) ')
    resposta_disco=int(input())

    for i in range(1,resposta_disco+1):
            i= Disco(i)
            t1.empilha(i)

def perguntar_t():

    print('De qual torre você deseja mover o disco? ')
    reposta_torre=input('')

    if reposta_torre== 'B':
        if reposta_torre == t2.get_nome():
            mover_disco(t2)
            print_torre()
            return perguntar_t()

    elif reposta_torre == 'C':
        if reposta_torre == t3.get_nome():
            mover_disco(t3)
            print_torre()
            return perguntar_t()

    elif reposta_torre == 'A':
        if reposta_torre == t1.get_nome():
            mover_disco(t1)
            print_torre()
            return perguntar_t()
    else:
        print('\nOpção invalida! Digite apenas A ou B ou C\n')
        return perguntar_t()

def print_torre():
    t1.to_string_torre()
    t2.to_string_torre()
    t3.to_string_torre()

def mover_disco(self):
    opcao=input('Para qual torre você deseja mover o disco ? ')
    if t2.get_nome()== opcao:
        self.esta_vazia()
        disco=self.desempilha(opcao)
        if disco.get_peso() < t2.torre_discos_peso():
            t2.empilha(disco)
        else:
            print('\nMovimento invalido ! Não pode colocar um disco mais pesado em um disco mais leve.\n')
            return perguntar_t()




if __name__ == '__main__':
    t1 = Torre('A', [])
    t2 = Torre('B', [])
    t3 = Torre('C', [])
    d1= Disco(3)
    t2.empilha(d1)
    t3.empilha(d1)
menu()