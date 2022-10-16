from Torre import Torre
from Disco import Disco

'''for i in range(1,9):
    i = Disco(i)'''

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

            return  menu()

    else:
        print('\nOpção invalida!Digite apenas 1 ou 2')
        return menu()

def star():

    instanciar_d()
    print_torre()
    perguntar_t()

def instanciar_d():
    print('Com quantos discos você que jogar? (OBS: no mínimo 3 discos) ')
    resposta_disco=int(input())

    if resposta_disco == 3:
        d1 = Disco(1)
        d2 = Disco(2)
        d3 = Disco(3)
        t1.empilha(d1)
        t1.empilha(d2)
        t1.empilha(d3)

    elif resposta_disco== 4:
        d1 = Disco(1)
        d2 = Disco(2)
        d3 = Disco(3)
        d4 = Disco(4)
        t1.empilha(d1)
        t1.empilha(d2)
        t2.empilha(d3)
        t2.empilha(d4)

def perguntar_t():
    print('De qual torre você deseja mover o disco? ')
    reposta_torre=input('')

    if reposta_torre== 'B':
        print()

    elif reposta_torre == 'C':
        print()

    elif reposta_torre == 'A':
        if reposta_torre == t1.get_nome():
            t1.mover_disco('A','B')
            print_torre()
    else:
        print('\nOpção invalida! Digite apenas A ou B ou C\n')
        return perguntar_t()

def print_torre():
    t1.to_string_torre()
    t2.to_string_torre()
    t3.to_string_torre()







if __name__ == '__main__':

    t1 = Torre('A', [])
    t2 = Torre('B', [])
    t3 = Torre('C', [])

''' d1 = Disco(1)
    d2 = Disco(2)
    d3 = Disco(3)
    d4 = Disco(4)
    d5 = Disco(5)
    d6 = Disco(6)
    d7 = Disco(7)
    d8 = Disco(8)
    d9 = Disco(100)'''

''' t1.empilha(d4)
    t1.empilha(d5)
    t1.empilha(d6)
    t1.empilha(d7)
    t1.empilha(d8)
    t1.empilha(d9)'''

menu()


